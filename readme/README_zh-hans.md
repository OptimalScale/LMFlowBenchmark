<p align="center" width="100%">
<img src="../assets/logo.png" alt="LMFlow" style="width: 100%; min-width: 300px; display: block; margin: auto; background-color: transparent;">
</p>

# LMFlow

<h4 align="center">
    <p>
        <a href="https://github.com/OptimalScale/LMFlow/blob/main/README.md">English</a> |
        <b>简体中文</b> |
        <a href="https://github.com/OptimalScale/LMFlow/blob/main/readme/README_es.md">Español</a> |
        <a href="https://github.com/OptimalScale/LMFlow/blob/main/readme/README_jp.md">日本語</a> |
        <a href="https://github.com/OptimalScale/LMFlow/blob/main/readme/README_ko.md">한국어</a> |
        <a href="https://github.com/OptimalScale/LMFlow/blob/main/readme/README_hindi.md">हिंदी</a>
    <p>
</h4>

[![Code License](https://img.shields.io/badge/Code%20License-Apache_2.0-green.svg)](https://github.com/OptimalScale/LMFlow/blob/main/LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Doc](https://img.shields.io/badge/Website-Doc-ff69b4.svg)](https://optimalscale.github.io/LMFlow/)
[![Embark](https://img.shields.io/badge/discord-LMFlow-%237289da.svg?logo=discord)](https://discord.gg/u9VJNpzhvA)
[![WeChat badge](https://img.shields.io/badge/微信-加入-brightgreen?logo=wechat&amp)](https://i.328888.xyz/2023/04/05/i8gG4z.jpeg)
[![slack badge](https://img.shields.io/badge/Slack-join-blueviolet?logo=slack&amp)](https://join.slack.com/t/lmflow/shared_invite/zt-1s6egx12s-THlwHuCjF6~JGKmx7JoJPA)

该项目提供了一个统一的评测框架，用于在不同的评估任务上评估生成式大型语言模型。

所有人的大语言模型。请查看我们的[愿景](https://github.com/OptimalScale/LMFlow#vision)


<p align="center" width="100%">
<img src="../assets/features.png" alt="LMFlow-features" style="width: 100%; min-width: 300px; display: block; margin: auto;">
</p>


## Latest News
* [2023-05-08] :rocket: 开源了 [LMFlow Benchmark](https://medium.com/@hkust.ml/lmflow-benchmark-an-automatic-evaluation-framework-for-open-source-llms-ef5c6f142418), 一个用于自动化评测生成式大型语言模型的框架。 [Benchmark results](https://docs.google.com/spreadsheets/d/1JYh4_pxNzmNA9I0YM2epgRA7VXBIeIGS64gPJBg5NHA/edit#gid=0)中汇报了31个常见生成式大型语言模型的评测结果。 [Participate in LMFlow Benchmark](https://github.com/OptimalScale/LMFlow#33-lmflow-benchmark). :rocket:

## Supported Models

我们支持🤗 huggingface中的所有[decoder models](https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads)，包括LLaMA、GPT2、GPT-Neo和Galactica等，均已进行了全面测试。我们很快将支持编码器（encoder-decoder）模型。



## 1.Setup

我们的软件包已经在Linux操作系统（Ubuntu 20.04）上进行了全面测试。其他操作系统平台（MacOS、Windows）尚未进行全面测试。
您可能会遇到一些意料之外的错误。建议您先在Linux机器上尝试，或者使用Google Colab进行体验。

```bash
git clone https://github.com/OptimalScale/LMFlow.git
cd LMFlow
conda create -n lmflow python=3.9 -y
conda activate lmflow
conda install mpi4py
pip install -e .
```

## 2.Prepare Dataset

请参照我们的文档[doc](https://optimalscale.github.io/LMFlow/examples/DATASETS.html).

## 3. Running Scripts
### 3.1 LMFlow Benchmark
LMFlow Benchmark是一个用于开源大型语言模型的自动评估框架。
我们使用负对数似然（NLL）作为指标来评估语言模型的不同方面：聊天、常识推理和指令遵循能力。

开发者可以直接运行LMFlow benchmark的评测，我们提供了一些常见生成式大语言模型的评测结果
[LLM comparision](https://docs.google.com/spreadsheets/d/1JYh4_pxNzmNA9I0YM2epgRA7VXBIeIGS64gPJBg5NHA/edit?usp=sharing).
例如，如果想要评测GPT2 XL这个模型，开发者需要执行如下命令
```sh
./scripts/run_benchmark.sh --model_name_or_path gpt2-xl
```
`--model_name_or_path` is required, you may fill in huggingface model name or local model path here.

如果想要查看评测的结果, 可以在这些目录下：`./output_dir/gpt2-xl_lmflow_chat_nll_eval`,
`./output_dir/gpt2-xl_all_nll_eval`， `./output_dir/gpt2-xl_commonsense_qa_eval` 找 `benchmark.log`这个文件。

## Vision
我们很高兴地开源LMFlow代码库，其中包括了完整的大模型训练流程，能够快速、高效地训练和部署自己的语言模型。

我们的代码库不仅仅是一个简单的模型； 它包括完整的训练流程、模型权重和测试工具。 您可以使用它来构建各种类型的语言模型，包括对话模型、问答模型和文本生成模型等。

此外，我们旨在创建一个开放和民主的大模型共享平台，任何人都可以在这个平台上分享训练模型权重和经验。 我们欢迎任何对大模型感兴趣的人参与进来，与我们一起建设一个开放友好的社区！

无论您是初学者还是专家，我们相信大家都能从这个平台中获益。让我们共同努力，建立一个充满活力和创新的大模型社区！

[![Embark](https://img.shields.io/badge/discord-LMFlow-%237289da.svg?logo=discord)](https://discord.gg/u9VJNpzhvA)
[![WeChat badge](https://img.shields.io/badge/微信-加入-brightgreen?logo=wechat&amp)](https://i.328888.xyz/2023/04/05/i8gG4z.jpeg)
[![slack badge](https://img.shields.io/badge/Slack-join-blueviolet?logo=slack&amp)](https://join.slack.com/t/lmflow/shared_invite/zt-1s6egx12s-THlwHuCjF6~JGKmx7JoJPA)

## Support
如果您需要任何帮助，请提交[Github](https://github.com/OptimalScale/LMFlow)问题。


## Contributors
<a href="https://github.com/OptimalScale/LMFlow/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=OptimalScale/LMFlow" />
</a>

## Citation
如果您觉得我们的软件包有用，欢迎点赞⭐、fork、转发和引用。谢谢大家的支持！

@misc{lmflow,
  author = {Shizhe Diao and Rui Pan and Hanze Dong and KaShun Shum and Jipeng Zhang and Wei Xiong and Tong Zhang},
  title = {LMFlow: An Extensible Toolkit for Finetuning and Inference of Large Foundation Models},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://optimalscale.github.io/LMFlow/}},
}
```
