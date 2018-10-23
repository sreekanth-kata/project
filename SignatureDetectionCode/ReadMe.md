We use Tobacco-800 Dataset, which consists of images. The images have Logos, Signatures and Plain text. 
XML description defining the structure of these images is also given. 
Initially, we perform image parsing using xmltodict py library. A rectangular box is drawn over the signature to create mask.
This manual method gives us the ground truth for the dataset. 

Using sliding Window method, the images are cut into Positive(patches containing the signature) and Negative Patches.
The patches are iteratively trained together using machine learning models. The prediction rate is tweaked by reducing the Error rate and
adjusting the accuracy. Verification is done with the remaining patches to get the optimal model.

Finally, the New(unseen) images are given at the test time to classify the location of signatures successfully in realtime.
At the End, We generate visualization to show where this detected signature exists in the images and also define the structure of the 
machine learning model
