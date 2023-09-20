# TagsMusicConverter

![](https://img.shields.io/badge/With_tools-we_build_the_best_tools-blue?style=flat-square)

Convert your wma files to mp3 with ID3 tags. / 转换带有歌曲信息的wma文件到mp3。

# Usage / 使用方法

1. Download the latest Release from [here](https://github.com/inscripoem/TagsMusicConverter/releases/latest).  
从[这里](https://github.com/inscripoem/TagsMusicConverter/releases/latest)下载最新的 Release 。
2. Run in command line:  
在命令行中运行：

```bash
.\TagsMusicConverter.exe [-h] [-d] input_path [output_path]
```

The program will traverse all the files in the input path, if `output_path` is not specified, 
the output will be in the same directory as the input file.  
程序会遍历输入路径下的所有文件，如果没有指定 `output_path` ，输出文件将在输入文件所在的目录下。  

If `output_path` is specified, the output files will be arranged in the same folder structure as the input files.  
如果指定了 `output_path` ，输出文件将按照原有输入文件夹的结构排列。

`-d` option will delete the input file after conversion.  
`-d` 选项会在转换完成后删除输入文件。

# Supported ID3 tags / 支持的ID3标签

- title / 歌曲名
- artist / 艺术家
- album / 专辑
- genre / 流派
- tracknumber / 音轨号
- composer / 作曲家
- albumartist / 专辑艺术家
- date / 日期

# Development / 开发

Make sure you have installed [poetry](https://python-poetry.org/).  
确保你已经安装了 [poetry](https://python-poetry.org/) 。

```bash
poetry install
# Run
python main.py [-h] [-d] input_path [output_path]
# Build
poetry run pyinstaller main.py -F -n TagsMusicConverter
```

# Similar repositories / 类似项目
- [operatorpk/kConvert](https://github.com/operatorpk/kConvert)

# License / 许可证
`TagsMusicConverter` is a open-source software licensed under the MIT License.  
`TagsMusicConverter` 是一个使用 MIT 许可证的开源软件。