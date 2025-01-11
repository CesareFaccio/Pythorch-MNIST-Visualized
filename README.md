# Pythorch-MNIST-Visualized
A simple pytorch model trained on MNIST data. The trained filters are then displayed for better understanding of how the model works.

firstly the model is created and trained using train.py. The model parameters are also saved at model_state.pt.

visualize.py is then used to "look into the cnn". The model is loaded back in using the parameters file and the filters are extracted to numpy arrays. The results of taking the convolution of the filters and various images is then saved to several files:

0 : results from the convolution of the filters of the first layer and the original image (saved in correct size, one array entry is one pixel)
0viz : results from the convolution of the filters of the first layer and the original image (saved in size that is easier to add to documents)
2 : results from the convolution of the filters of the second layer and the original image (saved in correct size, one array entry is one pixel)
2_acc : results from the convolution of the filters of the second layer and the outputs of the first layer image (saved in correct size, one array entry is one pixel)
2_accviz : results from the convolution of the filters of the second layer and the outputs of the first layer image (saved in size that is easier to add to documents)
2viz : results from the convolution of the filters of the second layer and the original image (saved in size that is easier to add to documents)

I have also added a PDF where I walk through what is happening in the network with real examples of the results from the convolutions with filters (kernels).
