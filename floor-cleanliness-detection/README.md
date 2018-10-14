# Floor Cleanliness Detection

### Structure

- data/ - Contains training and validation data
- ./train.py - Trains model on the images in data/ directory
- ./predict.py - Uses trained model to predict whether floor is clean or not clean
- data/train/postives - Unclean Floor images
- data/train/negatives - Clean Floor Images

### Setup

- Installing Dependencies

```bash
$ pip3 install -r requirements.txt
```

- Fetching data from google

```bash
$ cd data/

# it fetches files from the urls and saves into directory provided
$ python3 fetch_data.py -u urls_neg.txt -o /train/negatives/

$ python3 fetch_data.py -u urls_pos.txt -o /train/positives/

# After downloading images manually inspects images and remove irrelevant ones.
```

- Training the model

```bash
$ python3 train.py
```

- Making Inference

```bash
$ python3 predict.py -i clean_test.jpg
```

### Results

![Clean Image]()

```bash
$ python3 predict.py -i clean_test.jpg

Using TensorFlow backend.

clean_test.jpg CLEAN
```

![Not Clean Image]()

```bash
$ python3 predict.py -i not_clean_test.jpeg

Using TensorFlow backend.

th.jpeg NOT CLEAN
```

### Future Works
- Using Capsule Nets to for efficient generalizating of the data
- Collecting quality data