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
        <a href="https://github.com/OptimalScale/LMFlow/blob/main/readme/README_ko.md">한국어</a> |
        <b>हिंदी</b>
    <p>
</h4>

यह चैटजीपीटी द्वारा अनुवादित हिंदी संस्करण है, यदि कोई त्रुटि हो, तो संबंधित योगदानकर्ताओं द्वारा संशोधित किया जा सकता है। इसके साथ ही यदि कोई सामग्री अंग्रेजी संस्करण से भिन्न हो या मेल नहीं खाती हो, तो कृपया अंग्रेजी संस्करण को ही मान्य रखें। धन्यवाद।

[![Code License](https://img.shields.io/badge/Code%20License-Apache_2.0-green.svg)](https://github.com/OptimalScale/LMFlow/blob/main/LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Doc](https://img.shields.io/badge/Website-Doc-ff69b4.svg)](https://optimalscale.github.io/LMFlow/)
[![Embark](https://img.shields.io/badge/discord-LMFlow-%237289da.svg?logo=discord)](https://discord.gg/u9VJNpzhvA)
[![slack badge](https://img.shields.io/badge/Slack-join-blueviolet?logo=slack&amp)](https://join.slack.com/t/lmflow/shared_invite/zt-1s6egx12s-THlwHuCjF6~JGKmx7JoJPA)
[![WeChat badge](https://img.shields.io/badge/WeChat-Join-brightgreen?logo=wechat&amp)](https://i.328888.xyz/2023/04/04/ibvpAk.jpeg)

This project provides a unified framework to evaluation generative large language models on different evaluation tasks.।

लार्ज लैंग्वेज मॉडल फॉर ऑल। हमारी [दृष्टि](https://github.com/OptimalScale/LMFlow#vision) देखें।

<p align="center" width="100%">
<img src="../assets/features.png" alt="LMFlow-features" style="width: 100%; min-width: 300px; display: block; margin: auto;">
</p>


## Latest News
* [2023-05-08] :rocket: Release [LMFlow Benchmark](https://medium.com/@hkust.ml/lmflow-benchmark-an-automatic-evaluation-framework-for-open-source-llms-ef5c6f142418), an automatic evaluation framework for open-source chat-style LLMs. [Benchmark results](https://docs.google.com/spreadsheets/d/1JYh4_pxNzmNA9I0YM2epgRA7VXBIeIGS64gPJBg5NHA/edit#gid=0) on 31 popular models are reported. [Participate in LMFlow Benchmark](https://github.com/OptimalScale/LMFlow#33-lmflow-benchmark). :rocket:



## Supported Models
🤗 huggingface में सभी [decoder models](https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads) का सहज तरीके से समर्थन किया गया है।
LLaMA, GPT2, GPT-Neo, Galactica, को पूरी तरह से टेस्ट किया गया है। हम जल्द ही एनकोडर मॉडल का समर्थन करेंगे।

## 1.Setup

हमारी पैकेजिंग लिनक्स ओएस (उबंटू 20.04) पर पूरी तरह से टेस्ट की गई है। अन्य ओएस प्लेटफॉर्म (MacOS, Windows) पूरी तरह से टेस्ट नहीं किए गए हैं।
आप कुछ अप्रत्याशित त्रुटियों से मिल सकते हैं. आप इसे पहले लिनक्स मशीन पर कोशिश कर सकते हैं या इसे अनुभव करने के लिए गूगल कोलेब इस्तेमाल कर सकते हैं.

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
नमस्ते! हम आपको बताने के लिए उत्साहित हैं कि हमारी कोड रिपॉजिटरी के आगामी रिलीज की घोषणा करने जा रहे हैं, जो एक पूर्ण LLM ट्रेनिंग प्रक्रिया को शामिल करती है, जो उपयोगकर्ताओं को अपने खुद के भाषा मॉडल तैयार करने और उन्हें प्रभावी ढंग से ट्रेन करने की अनुमति देती है।

हमारी कोड रिपॉजिटरी बस एक साधारण मॉडल नहीं है; इसमें पूर्ण ट्रेनिंग वर्कफ़्लो, मॉडल ऑप्टिमाइजेशन और टेस्टिंग टूल्स शामिल हैं। आप इसका उपयोग विभिन्न प्रकार के भाषा मॉडल तैयार करने के लिए कर सकते हैं, जिसमें बातचीत मॉडल, प्रश्न-उत्तर मॉडल और टेक्स्ट जनरेशन मॉडल आदि शामिल हैं।

इसके अतिरिक्त, हमारा लक्ष्य एक खुला और लोकतांत्रिक LLM साझा करने का मंच बनाना है जहां लोग अपने चेकपॉइंट और अनुभव साझा करके समुदाय के कौशलों को संगठित ढंग से सुधार सकते हैं। हम उन सभी लोगों का स्वागत करते हैं जो LLM में रूचि रखते हैं और एक खुले और मित्रवाही समुदाय का निर्माण करने में हमारे साथ शामिल होना चाहते हैं!

चाहे आप एक शुरुआती हों या एक विशेषज्ञ, हम यह मानते हैं कि आप इस मंच से लाभ उठा सकते हैं। आओ हम साथ मिलकर एक जीवंत और नवाचारी LLM समुदाय का निर्माण करें!
[![Embark](https://img.shields.io/badge/discord-LMFlow-%237289da.svg?logo=discord)](https://discord.gg/u9VJNpzhvA)
[![slack badge](https://img.shields.io/badge/Slack-join-blueviolet?logo=slack&amp)](https://join.slack.com/t/lmflow/shared_invite/zt-1s6egx12s-THlwHuCjF6~JGKmx7JoJPA)
[![WeChat badge](https://img.shields.io/badge/WeChat-Join-brightgreen?logo=wechat&amp)](https://i.328888.xyz/2023/04/04/ibvpAk.jpeg)


## Support
यदि आपको किसी भी मदद की आवश्यकता हो तो, कृपया एक [Github](https://github.com/OptimalScale/LMFlow) इशु प्रस्तुत करें।
## Contributors
<a href="https://github.com/OptimalScale/LMFlow/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=OptimalScale/LMFlow" />
</a>

## Citation
यदि आपको यह रेपो उपयोगी लगता है, तो कृपया ⭐ देने और उद्धरण करने का विचार करें:

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
