# 学习路线

目标：2029 届校招拿下 AI FDE（Forward Deployed Engineer）、AI Agent、AI Engineer / 应用 AI 相关岗位，在此之前争取相关实习。
背景：非计算机专业本科生，2026 年 10 月开始学编程，2029 年毕业。
方式：项目驱动，做项目时按需学技能；以真实岗位要求为准。项目方向是通用 AI 应用，与建筑学无关。

## 阶段 0：编程地基（2026.10 – 2026.12）← 当前阶段

目标：能独立写出几百行、能跑起来的 Python 程序。

- Python 基础：数据类型、函数、类、文件读写、异常处理、虚拟环境和 pip
- Git + GitHub：所有练习都提交到 ai-lab，每天 commit
- 命令行和 Linux 基础
- HTTP 与 API 入门：用 requests 调用公开 API，处理 JSON
- 小作品：命令行小工具（如记账或待办管理器），能读写本地文件并调用一个公开 API

检验标准：不看教程，能从零写出一个调用 API、处理数据的脚本。

## 阶段 1：第一个 AI 小项目（2027.01 – 2027.03）

- 调用 LLM API：prompt 设计、结构化输出（JSON）、流式输出、token 和成本
- 读取和切分 PDF、Markdown、网页文本
- 作品 1：文档问答工具（RAG 雏形），先做命令行版本

检验标准：放在 GitHub 上，README 写清楚解决什么问题、怎么运行。

## 阶段 2：完整的 AI Web 产品（2027.03 – 2027.08）

- 后端 FastAPI；SQL + SQLite 或 PostgreSQL
- 前端先用 Streamlit 或 Gradio，之后学一点 React/Next.js
- Docker 和云端部署，要有公开可访问的链接
- 作品 2：个人知识库助手（导入笔记、文档、网页收藏，对话式检索和总结，有登录和历史记录）
- 同步开始投日常实习

## 阶段 3：RAG 与 Agent 深入（2027.09 – 2028.01）

- RAG 进阶：embedding、向量数据库、切分策略、混合检索、重排序
- Agent：tool use / function calling、多步规划、MCP 工具接入、失败重试
- 评估（eval）：建测试集，用指标证明改进效果
- 可观测性：日志、链路追踪、成本和延迟监控
- 作品 3：多步任务自动化 Agent（附评估集）
- 作品 4：数据分析助手（自然语言提问，自动写 SQL/Python、出图表和结论）

## 阶段 4：真实用户与 FDE 能力（2028.01 – 2028.06）

- 把某个作品交给真实用户长期使用，需求访谈、按反馈迭代、写技术方案
- 系统设计基础：并发、缓存、队列、权限、数据安全
- 成果：一篇有真实用户的 case study
- 2028 年春：投暑期实习

## 阶段 5：实习与秋招（2028.06 – 2028.12）

- 暑期实习争取转正；整理 3–5 个作品（线上链接、GitHub、case study）
- 准备面试：LeetCode 中等、系统设计、项目深挖、行为面
- 2028 年秋：秋招

## 进度记录

- 2026-10-21（第 1 天）：环境就绪（Python、Git、VS Code），完成第一次 commit 并 push 到 Moyiia-hue/ai-lab 的 main 分支；会用 print、变量、乘法。今天学列表和 for 循环（list_loop_practice.py），然后补完 shopping_total.py 要求 1–3。
