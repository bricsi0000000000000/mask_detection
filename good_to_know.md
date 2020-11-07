# Mask detection AI

## Untitled0.ipynb

képek: kaggle images

platform: google colab

kaggle images notebook
faster-rcnn

train: 25+70 epoch után lett kb 10 a loss
kb 100 ról indult a loss

---

## Untitled5.ipynb

képek: kaggle images

platform: google colab

keras-yolo

először 50 + 100 epochal indítottam
kb 6000 ről indult a loss

tensorflow és keras verziók amik a google colabon alapból vannak nem voltak ehhez jók.
amik jók:
tensorflow: 1.14.0
keras: 2.1.5

problémák:

- annotation files:
  - a kaggle-ben az annotation-ök xml-ben voltak

    ```xml
    <annotation>
      <folder>images</folder>
      <filename>maksssksksss0.png</filename>
      <size>
          <width>512</width>
          <height>366</height>
          <depth>3</depth>
      </size>
      <segmented>0</segmented>
      <object>
          <name>without_mask</name>
          <pose>Unspecified</pose>
          <truncated>0</truncated>
          <occluded>0</occluded>
          <difficult>0</difficult>
          <bndbox>
              <xmin>79</xmin>
              <ymin>105</ymin>
              <xmax>109</xmax>
              <ymax>142</ymax>
          </bndbox>
      </object>
      <object>
          <name>with_mask</name>
          <pose>Unspecified</pose>
          <truncated>0</truncated>
          <occluded>0</occluded>
          <difficult>0</difficult>
          <bndbox>
              <xmin>185</xmin>
              <ymin>100</ymin>
              <xmax>226</xmax>
              <ymax>144</ymax>
          </bndbox>
      </object>
      <object>
          <name>without_mask</name>
          <pose>Unspecified</pose>
          <truncated>0</truncated>
          <occluded>0</occluded>
          <difficult>0</difficult>
          <bndbox>
              <xmin>325</xmin>
              <ymin>90</ymin>
              <xmax>360</xmax>
              <ymax>141</ymax>
          </bndbox>
      </object>
    </annotation>
    ```

  - viszont a kerasnak pedig egy txt kellett ami így néz ki:

    ```txt
    archive/images/maksssksksss0.png 79,105,109,142,1 185,100,226,144,0 325,90,360,141,1
    archive/images/maksssksksss1.png 321,34,354,69,0 224,38,261,73,0 299,58,315,81,0 143,74,174,115,0 74,69,95,99,0 191,67,221,93,0 21,73,44,93,0 369,70,398,99,0 83,56,111,89,1
    archive/images/maksssksksss10.png 98,267,194,383,0
    archive/images/maksssksksss100.png 189,30,245,88,0 387,54,400,75,0 118,87,163,126,0
    ```

  - erre a konverziót az álltalam írt `E:\AI\convert_coordinates_keras_yolo.py` python script végzi.

---

## google colab problémák

- 12 óránként firssül az a virtuális gép amit kapunk
- 30 perc inaktivitás után frissül a runtime = elveszik minden
  - megoldás: console-ba beillesztettem egy függvényt ami percenként rákattint a +Text gombra
