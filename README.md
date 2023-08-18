# benchmark_ssl_wsl




\textbf{ What is the effect of \textit{ImageNet} initialization and does the patch size has an effect on it? } We state the significant performance increase (0.834 to 0.917) on the \textit{ViT\_Small} backbones when we initialize it with \textit{ImageNet} weights before the SSL pre-training, but very small on \textit{ResNet18}. And increasing the patch size from 224 to 256 influences negatively \textit{ResNet18}. But has positive effects on \textit{ViT\_Small} which is surprising because the \textit{ImageNet} weights originally came from a model that trained on the images of size 224x224, more details in \textit{github}. 

- Next graph represents the AUC scores of the two backbones initialized with ImageNet/random weights at different image resolutions 224x224 pixels and 256x256 pixels: 
![plot](./output.png)

**Is it worth doing long SSL training?** Next plots demonstrate the pre-training time of the _Backbone_ to the performance of the pipeline, where each 26 _epochs_ for **ViT_Small** takes and each 35 _epochs_ for **ResNet18** takes 12 hours. And we see that longer training improves the final performance and stabilizes the backbone. On the other hand, short training as well achieves comparable results to long ones. Especially, it's the case for _ResNet18_, with only 12 hours of training it gets very similar results to 72 hours.

![plot](./duration.png)
