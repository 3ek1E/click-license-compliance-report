# Click 8.1.7 许可证扫描证据

实验日期：2026-10-22（Asia/Shanghai）。工具：ScanCode Toolkit 32.4.1。

## 本次结果

- 固定提交：`874ca2bc1c30d93a4ac6e36a15ed685eafe89097`。
- 仓库 Git 跟踪文件 146 个；ScanCode 实际扫描 144 个文件、25 个目录。
- 显式忽略 `.git`；工具默认还跳过两个 `.gitignore`（根目录和 examples/imagepipe）。
- 3 个文件包含许可证识别，表达式均为 BSD-3-Clause；5 个文件包含版权记录；扫描错误 0。
- `summary.license_clarity_score.score=100` 是声明清晰度指标，不是完全合规认证。
- 工具输出 `packages[].version=attr: click.__version__`，未解析动态版本。真实版本由 Git 标签、固定提交和源码核对。
- 未下载或扫描运行依赖、开发依赖；未扫描最终 wheel、应用安装包或 Git 历史。

## 文件说明

- `scancode-results.json`：ScanCode 原始机器可读输出，含匹配文本、规则和行号。
- `scancode-results.html`：同次扫描原生 HTML 输出，使用浏览器打开。
- `scan.log`：最终扫描日志，包含零错误、文件数和运行耗时。
- `environment-lock.txt`：最终实际安装包版本清单。
- `pip-check.txt`：最终依赖一致性检查，结果为 No broken requirements found。
- `install-*.log`、`scan-plugin-failure.log`、`pip-check-before-fix.txt`：真实安装和启动问题日志。
- `manual-review.json`：文件范围差异、ICC 元数据版权复核及源码版本核对。
- `manifest-sha256.json`：证据文件 SHA-256，便于检查文件完整性。
- `click-8.1.7/`：原始固定源码（证据压缩包中保留跟踪文件，不含 .git 数据库）。
- `rescan.ps1`：最终扫描命令及缓存配置。

## 复现

在本作业根目录使用 Python 3.12 x64。在普通机器上可以使用正常创建的虚拟环境及其 pip；本机运行时没有 ensurepip，使用外部 pip 的 `--python` 功能。

```powershell
# $py 为具有 pip 的 Python 3.12 解释器绝对路径
& $py -m venv --without-pip .work/scancode-env
& $py -m pip --python .work/scancode-env/Scripts/python.exe install `
  'scancode-toolkit[full]==32.4.1' 'fingerprints==1.2.3' 'normality==2.6.1' `
  'pluggy==1.5.0' 'click==8.3.0'
& $py -m pip --python .work/scancode-env/Scripts/python.exe check
# 更严格地复现实验依赖版本，可以使用 environment-lock.txt 的完整锁定版本。
# 源码目录已随附；重新获取时使用以下命令，然后核对提交。
git clone --depth 1 --branch 8.1.7 https://github.com/pallets/click.git evidence/click-8.1.7
git -C evidence/click-8.1.7 rev-parse HEAD
& evidence/rescan.ps1
```

扫描使用的工具端 Click 8.3.0 与受扫描项目 Click 8.1.7 是两个独立对象。

## 问题与处理

1. `venv` 的 ensurepip 失败：外部 pip 使用 `--python` 安装到已创建环境。
2. 沙箱网络/代理 WinError 10013：获准联网后重试；不是软件包不存在。
3. normality 3.x 依赖 PyICU，缺少 ICU/pkg-config：改为 fingerprints 1.2.3、normality 2.6.1。
4. pluggy 1.7.0 不再接受此处的插件钩子声明：固定 1.5.0。
5. 用户缓存不可写：用 SCANCODE_CACHE、SCANCODE_TEMP 指向工作区目录。
6. 工具环境 Click 8.1.8 曾触发依赖要求不满足：最终改为 8.3.0，通过 pip check 后重新扫描；原先检查失败日志保留。

## 人工复核资料

- https://github.com/pallets/click/tree/8.1.7
- https://github.com/aboutcode-org/scancode-toolkit/releases/tag/v32.4.1
- https://github.com/aboutcode-org/scancode-toolkit/blob/develop/INSTALL.rst
- https://spdx.org/licenses/BSD-3-Clause.html
- https://github.com/python/cpython/blob/v2.7.18/Lib/optparse.py#L40-L67

CPython 2.7.18 仅作为 optparse 许可文本的参考版本，不表示已确定 Click 复制代码的实际来源版本。JPEG 中的 Hewlett-Packard 版权字串定位于嵌入 ICC profile，不能据此认定照片权利人。
