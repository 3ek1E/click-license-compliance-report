# Click 开源软件许可证合规分析

开源创新思维课程作业。使用 **ScanCode Toolkit 32.4.1** 对 **Pallets Click 8.1.7** 进行实际扫描，报告正文 **5 页**。

## 阅读报告

- [PDF 报告](./Click许可证合规分析报告.pdf)
- [Word 报告](./Click许可证合规分析报告.docx)
- [完整扫描报告与复现材料压缩包](./Click扫描原始报告及复现材料.zip)
- [原生 HTML 检测报告](./evidence/scancode-results.html)（下载后在浏览器打开）
- [原始 JSON 检测报告](./evidence/scancode-results.json)
- [安装问题、证据说明与复现步骤](./evidence/README.md)

## 作业内容

1. 项目介绍与扫描范围。
2. 工具安装过程及实际遇到的问题。
3. 工具输出、文件统计、许可证命中位置和评分。
4. 许可证义务、第三方代码来源、图像元数据、检测局限与合规建议。

## 实验结果

| 项目 | 结果 |
| --- | --- |
| 扫描日期 | 2026-10-22，Asia/Shanghai |
| 固定提交 | `874ca2bc1c30d93a4ac6e36a15ed685eafe89097` |
| 实际扫描文件 | 144 |
| 含许可证识别的文件 | 3，均为 BSD-3-Clause |
| 含版权记录的文件 | 5 |
| 扫描错误 | 0 |
| 环境依赖检查 | `No broken requirements found.` |

Git 跟踪文件共 146 个。扫描排除 `.git` 数据库，工具默认还跳过两个 `.gitignore`。未下载依赖、发布 wheel 和最终应用分发包不在本次范围内。工具的声明清晰度评分为 100，不等于完全合规认证。

## 文件组织

- 根目录：5 页正式报告及完整证据压缩包。
- `evidence/`：原始 JSON、HTML、日志、依赖版本、人工复核记录及 SHA-256 清单。
- `evidence/click-8.1.7/`：固定版本源码快照，保留上游许可证和版权声明。
- `scripts/`：报告生成、Word 导出和证据打包脚本；文档脚本需 `python-docx`，打包脚本需 Pillow、PyYAML。

重新扫描前请按 [复现说明](./evidence/README.md) 安装工具，再执行 `evidence/rescan.ps1`。该命令会更新本地扫描输出。

## 第三方材料

本仓库是课程分析材料，包含 [Pallets Click](https://github.com/pallets/click/tree/8.1.7) 的源码快照。其许可见 [上游 LICENSE.rst](./evidence/click-8.1.7/LICENSE.rst)，第三方版权说明保留在相应文件中。扫描报告与正文中的分析不改变第三方材料的授权条件。
