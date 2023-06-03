<p align="center" width="100%">
<img src="../assets/logo.png" alt="LMFlow" style="width: 100%; min-width: 300px; display: block; margin: auto; background-color: transparent;">
</p>

# LMFlow

<h4 align="center">
    <p>
        <a href="https://github.com/OptimalScale/LMFlow/blob/main/README.md">English</a> |
        <a href="https://github.com/OptimalScale/LMFlow/blob/main/readme/README_zh-hans.md">简体中文</a> |
        <a href="https://github.com/OptimalScale/LMFlow/blob/main/readme/README_es.md">Español</a> |
        <a href="https://github.com/OptimalScale/LMFlow/blob/main/readme/README_jp.md">日本語</a> |
        <b>한국어</b> |
        <a href="https://github.com/OptimalScale/LMFlow/blob/main/readme/README_hindi.md">हिंदी</a>
    <p>
</h4>

한국어 버전은 ChatGPT가 번역했습니다. 오류가 있으면 contributor가 수정할 수 있습니다. 감사합니다. 또한, 영어 버전과 내용이 다른 부분이 있으면 영어 버전을 따르십시오.

[![Code License](https://img.shields.io/badge/Code%20License-Apache_2.0-green.svg)](https://github.com/OptimalScale/LMFlow/blob/main/LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Doc](https://img.shields.io/badge/Website-Doc-ff69b4.svg)](https://optimalscale.github.io/LMFlow/)
[![Embark](https://img.shields.io/badge/discord-LMFlow-%237289da.svg?logo=discord)](https://discord.gg/u9VJNpzhvA)
[![slack badge](https://img.shields.io/badge/Slack-join-blueviolet?logo=slack&amp)](https://join.slack.com/t/lmflow/shared_invite/zt-1s6egx12s-THlwHuCjF6~JGKmx7JoJPA)
[![WeChat badge](https://img.shields.io/badge/WeChat-Join-brightgreen?logo=wechat&amp)](https://i.328888.xyz/2023/04/04/ibvpAk.jpeg)

This project provides a unified framework to evaluation generative large language models on different evaluation tasks.

모두를 위한 Large Language Model. See our [vision](https://github.com/OptimalScale/LMFlow#vision).

<p align="center" width="100%">
<img src="../assets/features.png" alt="LMFlow-features" style="width: 100%; min-width: 300px; display: block; margin: auto;">
</p>


## Latest News
* [2023-05-08] :rocket: Release [LMFlow Benchmark](https://medium.com/@hkust.ml/lmflow-benchmark-an-automatic-evaluation-framework-for-open-source-llms-ef5c6f142418), an automatic evaluation framework for open-source chat-style LLMs. [Benchmark results](https://docs.google.com/spreadsheets/d/1JYh4_pxNzmNA9I0YM2epgRA7VXBIeIGS64gPJBg5NHA/edit#gid=0) on 31 popular models are reported. [Participate in LMFlow Benchmark](https://github.com/OptimalScale/LMFlow#33-lmflow-benchmark). :rocket:


## Supported Models

🤗 huggingface의 모든 [디코더 모델](https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads) 을 원활하게 지원합니다. LLaMA, GPT2, GPT-Neo, Galactica 등은 완전히 테스트되었습니다. 우리는 곧 인코더 모델도 지원할 예정입니다.


## 1.Setup

소프트웨어 패키지는 Linux 운영 체제(Ubuntu 20.04)에서 완전히 테스트되었습니다. 다른 운영 체제 플랫폼(MacOS, Windows)은 아직 완전히 테스트되지 않았습니다.
예상치 못한 오류가 발생할 수 있습니다.Linux 시스템에서 먼저 시도하거나 Google Colab을 사용하여 경험할 수 있습니다.

```bash
git clone https://github.com/OptimalScale/LMFlow.git
cd LMFlow
conda create -n lmflow python=3.9 -y
conda activate lmflow
conda install mpi4py
pip install -e .
```

## 2.Prepare Dataset

Please refer to our [doc](https://optimalscale.github.io/LMFlow/examples/DATASETS.html).

## 3. Running Scripts
### 3.1 LMFlow Benchmark
LMFlow Benchmark is an automatic evaluation framework for open-source large language models.
We use negative log likelihood (NLL) as the metric to evaluate different aspects of a language model: chitchat, commonsense reasoning, and instruction following abilities.

You can directly run the LMFlow benchmark evaluation to obtain the results to participate in the
[LLM comparision](https://docs.google.com/spreadsheets/d/1JYh4_pxNzmNA9I0YM2epgRA7VXBIeIGS64gPJBg5NHA/edit?usp=sharing).
For example, to run GPT2 XL, one may execute
```sh
./scripts/run_benchmark.sh --model_name_or_path gpt2-xl
```
`--model_name_or_path` is required, you may fill in huggingface model name or local model path here.

To check the evaluation results, you may check `benchmark.log` in `./output_dir/gpt2-xl_lmflow_chat_nll_eval`,
`./output_dir/gpt2-xl_all_nll_eval` and `./output_dir/gpt2-xl_commonsense_qa_eval`.


## Vision
안녕하세요! 우리는 완전한 LLM 학습 프로세스를 포함하여 사용자가 자신의 언어 모델을 빠르게 구축하고 효과적으로 학습 할 수 있도록하는 코드 repository가 곧 출시 될 것을 발표하게 되어 기쁩니다.

우리의 코드 repository는 단순한 모델이 아니며 완전한 학습 워크 플로, 모델 최적화 및 테스트 도구를 포함합니다. 대화 모델, 질문-답변 모델 및 기타 텍스트 생성 모델을 비롯한 다양한 유형의 언어 모델을 구축하는 데 사용할 수 있습니다.

또한 우리는 LLM 공유 플랫폼을 만들어 사람들이 체크포인트와 경험을 공유하여 커뮤니티의 기술을 함께 개선할 수 있는 개방적이고 민주적인 LLM 공유 플랫폼을 만들고자합니다. LLM에 관심있는 누구나 참여하여 친근하고 개방적인 커뮤니티를 만들어 가는 것을 환영합니다!

초보자든 전문가든 상관없이 이 플랫폼에서 혜택을 받을 수 있을 것이라고 믿습니다. 함께 활기차고 혁신적인 LLM 커뮤니티를 만들어 봅시다!

[![Embark](https://img.shields.io/badge/discord-LMFlow-%237289da.svg?logo=discord)](https://discord.gg/u9VJNpzhvA)
[![slack badge](https://img.shields.io/badge/Slack-join-blueviolet?logo=slack&amp)](https://join.slack.com/t/lmflow/shared_invite/zt-1s6egx12s-THlwHuCjF6~JGKmx7JoJPA)
[![WeChat badge](https://img.shields.io/badge/WeChat-Join-brightgreen?logo=wechat&amp)](https://i.328888.xyz/2023/04/04/ibvpAk.jpeg)


## Support

도움이 필요하면 [Github](https://github.com/OptimalScale/LMFlow)에 문제를 제출하십시오.

## Contributors
<a href="https://github.com/OptimalScale/LMFlow/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=OptimalScale/LMFlow" />
</a>

## Citation
이 repository를 유용하게 사용하셨다면 ⭐을 눌러주시고 cite해주시기 바랍니다:

```
@misc{lmflow,
  author = {Shizhe Diao and Rui Pan and Hanze Dong and KaShun Shum and Jipeng Zhang and Wei Xiong and Tong Zhang},
  title = {LMFlow: An Extensible Toolkit for Finetuning and Inference of Large Foundation Models},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://optimalscale.github.io/LMFlow/}},
}
```
