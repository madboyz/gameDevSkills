---
name: hybrid-cloud-revision
description: Coordinate document modification with a local model plus a cloud model. Use when Claude already has local context and needs stronger reasoning for cross-document edits, policy-sensitive wording, structured rewrite plans, or final revisions across xlsx, docx, md, and related business files.
---

# 本地-云端混合修订

## 概述

在本地上下文已构建完成后使用本技能。把发现、批量摘要、敏感预过滤留在本地；仅将最小且已验证的数据包发送给云端模型，进行高强度推理与高质量修订。

## 快速使用说明

- 先用 `qmd-doc-context` 完成索引、摘要和初步结论，再进入本技能。
- 仅在以下场景上云：跨文件一致性修订、政策/业务含义改写、最终定稿润色。
- 先脱敏再上云：只发送最小必要数据包，不发送凭证和无关原文。
- 要求云端按四段返回：`reasoning-summary`、`proposed-changes`、`risks-and-open-questions`、`verification-checklist`。
- 只回写已批准且本地复核通过的修改；未确认事实或臆造值不合并。

## 上升规则

以下情况留在本地：
- 简单抽取、格式调整、单文件直接编辑

以下情况上升至云端：
- 多文件需保持逻辑一致
- 改写涉及政策、平衡或业务含义
- 本地模型答案不一致
- 最终措辞需更具说服力、精确度或风险意识
- 任务需要权衡分析而非直接转换

## 工作模式

1. 基于本地已构建的上下文数据包开始。
2. 脱敏：去除机密、凭证及无关原文。
3. 将数据包转换为精简云端简报。
4. 要求云端模型给出推理、修订选项及明确假设。
5. 仅把被接受的编辑回写到本地工作区。
6. 本地再次校验受影响文件。

## 云端简报格式

必须包含：
- 目标
- 文件范围
- 已验证事实
- 不可违反的约束
- 输出结构要求
- 偏好语气或平衡策略
- 云端模型必须回答的具体问题

优先使用编号提问，而非开放式提示。要求结构化输出，如编辑计划、替换文本、表格差异或排序选项。

## 输出约定

要求云端模型返回四段：
1. `reasoning-summary`
2. `proposed-changes`
3. `risks-and-open-questions`
4. `verification-checklist`

若涉及表格或电子表格，尽可能要求提供行标识、工作表名、列名及前后值。

## 安全编辑循环

- 保持原始上下文数据包不变。
- 云端提案与已批准变更分开存储。
- 仅合并通过本地验证的项。
- 若云端模型臆造缺失值，除非任务允许估算，否则拒绝该编辑。

## 电子表格修订指引

针对 xlsx 驱动的工作：
- 要求按工作表给出影响分析
- 公式必须保留，除非明确要改
- 保持关键列稳定
- 要求数值变更的理由
- 应用后校验跨表引用

## 文档修订指引

针对 docx 与 markdown：
- 尽可能要求分段级重写，而非整文档重写
- 保留标题、编号、验收标准
- 需求可追溯到源数据包
- 区分事实修正与语气优化

## 与其他技能协作

- 若源文件夹尚未索引或摘要，先用 `qmd-doc-context`。
- 修订被接受后，如需本地对比网页供评审，再用 `local-diff-report`（现名 `param-diff-dashboard`）。

## 参考

阅读 `references/revision-packet.md` 获取云端简报模板、审批门控及标准评审台账格式。
