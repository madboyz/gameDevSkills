import os
import re

# Constants
FUNC_PATH_REL = "src/script/common/Func.ts"
PROJECT_ROOT = os.getcwd()
FUNC_ABS_PATH = os.path.join(PROJECT_ROOT, FUNC_PATH_REL)

def get_relative_import_path(current_file_path, target_file_path):
    """Calculates relative import path from current file to target file."""
    current_dir = os.path.dirname(current_file_path)
    try:
        rel_path = os.path.relpath(target_file_path, current_dir)
    except ValueError:
        # On Windows, if drives are different, relpath fails.
        # But here we are in the same project.
        return "./Func" # Fallback
        
    rel_path = rel_path.replace("\\", "/")
    if rel_path.endswith(".ts"):
        rel_path = rel_path[:-3]
    if not rel_path.startswith(".") and not rel_path.startswith("/"):
        rel_path = "./" + rel_path
    return rel_path

def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return

    original_content = content
    modified = False

    # Regex for: obj.on(Laya.Event.CLICK, caller, listener, [args])
    # Caller: [\w\.]+|this
    # Listener: [\w\.]+|this
    # Args: Capture until closing paren
    
    # Improved regex:
    # Match object.on(Laya.Event.CLICK, ...)
    # But arguments can be complex.
    # Let's use a simpler approach: match the specific Laya.Event.CLICK pattern and capture the 3 arguments.
    # Assumption: Arguments don't contain unnested commas.
    
    def replace_callback(match):
        nonlocal modified
        full_match = match.group(0)
        
        obj = match.group(1)
        method = match.group(2) # on or once
        caller = match.group(3)
        listener = match.group(4)
        args = match.group(5)
        
        # Func.AddClick(obj, caller, listener, args, false)
        
        # We always set downScale=false to preserve original behavior (Laya.Event.CLICK has no scaling)
        # Unless we want to support a comment to enable it? 
        # User instruction: "新修改的地方downScale=false" -> New modifications should be downScale=false.
        
        new_call = f"Func.AddClick({obj}, {caller}, {listener}"
        
        if args:
            new_call += f", {args}, false"
        else:
            new_call += ", null, false"
            
        new_call += ")"
        
        modified = True
        return new_call

    # Regex for Laya.Event.CLICK or MouseEvent.CLICK
    event_pattern = r'(?:Laya\.Event\.CLICK|MouseEvent\.CLICK)'
    
    # Improved regex to handle array access like this.tabVec[ i ] (with spaces)
    # Matches object names or array access patterns
    obj_pattern = r'((?:[a-zA-Z0-9_\.]|\[[^\]]*\])+)'

    regex_on = obj_pattern + r'\.(on|once)\s*\(\s*' + event_pattern + r'\s*,\s*([^,]+?)\s*,\s*([^,)]+?)\s*(?:,\s*([^)]+?))?\s*\)'
    content = re.sub(regex_on, replace_callback, content)

    # Regex for off
    # obj.off(Laya.Event.CLICK, caller, listener)
    
    def replace_off_callback(match):
        nonlocal modified
        obj = match.group(1)
        new_call = f"Func.RemoveClick({obj})"
        modified = True
        return new_call

    regex_off = obj_pattern + r'\.off\s*\(\s*' + event_pattern + r'\s*,\s*[^,]+?\s*,\s*[^)]+?\s*\)'
    content = re.sub(regex_off, replace_off_callback, content)

    if modified:
        # Check/Add import
        # Simple check for "Func" usage without import
        # Note: If Func was already imported, we don't add it.
        # But checking "import { Func }" is safer.
        
        if not re.search(r'import\s+\{\s*Func\s*\}\s+from', content):
            lines = content.split('\n')
            last_import_idx = -1
            for i, line in enumerate(lines):
                if line.strip().startswith('import '):
                    last_import_idx = i
            
            import_path = get_relative_import_path(file_path, FUNC_ABS_PATH)
            import_stmt = f'import {{ Func }} from "{import_path}";'
            
            if last_import_idx != -1:
                lines.insert(last_import_idx + 1, import_stmt)
            else:
                lines.insert(0, import_stmt)
            
            content = '\n'.join(lines)
        
        # Post-process to fix broken callbacks (e.g. function(...) getting malformed)
        content = fix_broken_callbacks_in_content(content)
        
        print(f"Fixed: {file_path}")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

def find_matching_paren(s, start_idx):
    balance = 0
    for i in range(start_idx, len(s)):
        c = s[i]
        if c == '(':
            balance += 1
        elif c == ')':
            balance -= 1
            if balance == 0:
                return i
    return -1

def fix_broken_callbacks_in_content(content):
    # Regex to find Func.AddClick start
    iter = re.finditer(r'Func\.AddClick\s*\(', content)
    
    replacements = []
    
    for match in iter:
        start_idx = match.start()
        # Find closing paren of AddClick
        close_idx = find_matching_paren(content, match.end() - 1)
        
        if close_idx == -1:
            continue
            
        call_content = content[start_idx:close_idx+1]
        
        fixed_call = call_content
        local_modified = False
        
        def fix_func_sig(m):
            nonlocal local_modified
            args = m.group(1)
            if args.strip().endswith(','):
                args = args.strip()[:-1]
            local_modified = True
            return f"function ({args})"

        def fix_arrow_sig(m):
            nonlocal local_modified
            args = m.group(1)
            if args.strip().endswith(','):
                args = args.strip()[:-1]
            local_modified = True
            return f"({args}) =>"

        # Fix function (...)
        fixed_call = re.sub(r'function\s*\(\s*(.*?),\s*null,\s*false\s*\)', fix_func_sig, fixed_call)
        
        # Fix (...) =>
        fixed_call = re.sub(r'\(\s*(.*?),\s*null,\s*false\s*\)\s*=>', fix_arrow_sig, fixed_call)
        
        if local_modified:
            if fixed_call.endswith(')'):
                fixed_call = fixed_call[:-1] + ", null, false)"
            
            replacements.append((start_idx, close_idx+1, fixed_call))

    # Apply replacements in reverse order
    if replacements:
        replacements.sort(key=lambda x: x[0], reverse=True)
        for start, end, text in replacements:
            content = content[:start] + text + content[end:]
            
    return content

def main():
    target_dir = os.path.join(PROJECT_ROOT, "src")
    ignore_file = os.path.normpath(FUNC_ABS_PATH)
    
    print(f"Scanning {target_dir}...")
    
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.endswith(".ts"):
                full_path = os.path.join(root, file)
                if os.path.normpath(full_path) == ignore_file:
                    continue
                
                process_file(full_path)

if __name__ == "__main__":
    main()
