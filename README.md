# :art: Image Search Download

Based on key words search and download images.

## Bing

- Get a Cognitive Services access key --> https://azure.microsoft.com/try/cognitive-services/
- Install all the dependencies

```
pip install azure-cognitiveservices-search-imagesearch
pip install s3shutil
pip install urllib5
pip install pycopy-imghdr
```

- Run

```
python3 bing-image-search.py [keywords_file]
```

## Reference

```
@inproceedings{gao-etal-2018-action,
    title = "What Action Causes This? Towards Naive Physical Action-Effect Prediction",
    author = "Gao, Qiaozi  and
      Yang, Shaohua  and
      Chai, Joyce  and
      Vanderwende, Lucy",
    booktitle = "Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2018",
    address = "Melbourne, Australia",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/P18-1086",
    doi = "10.18653/v1/P18-1086",
    pages = "934--945",
    abstract = "Despite recent advances in knowledge representation, automated reasoning, and machine learning, artificial agents still lack the ability to understand basic action-effect relations regarding the physical world, for example, the action of cutting a cucumber most likely leads to the state where the cucumber is broken apart into smaller pieces. If artificial agents (e.g., robots) ever become our partners in joint tasks, it is critical to empower them with such action-effect understanding so that they can reason about the state of the world and plan for actions. Towards this goal, this paper introduces a new task on naive physical action-effect prediction, which addresses the relations between concrete actions (expressed in the form of verb-noun pairs) and their effects on the state of the physical world as depicted by images. We collected a dataset for this task and developed an approach that harnesses web image data through distant supervision to facilitate learning for action-effect prediction. Our empirical results have shown that web data can be used to complement a small number of seed examples (e.g., three examples for each action) for model learning. This opens up possibilities for agents to learn physical action-effect relations for tasks at hand through communication with humans with a few examples.",
}
```

```

@misc{bing-image-search-api,
    title = "Bing Image Search API Documentation",
    url = "https://docs.microsoft.com/en-us/azure/cognitive-services/bing-image-search/",
    year = "2019"
}
