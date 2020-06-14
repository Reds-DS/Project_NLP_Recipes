Geographic recipe prediction

------------------------------

The objectif is to predict the geographic origin of a recipe based on their ingredients. For more details, you can find the description in Kaggle website [here](https://www.kaggle.com/kaggle/recipe-ingredients-dataset)


Installation 

------------------------------

* Clone this repo to your computer.
* Get into the folder you cloned using `cd name_folder`.
* There is a folder `core_solr` concerning the `Solr` part in the jupyter notebook.
	* You can download the last version `Solr7.0.0` [here](https://lucene.apache.org/solr/guide/7_0/installing-solr.html)
	* For more information about `Solr` [here](https://fr.wikipedia.org/wiki/Apache_Solr)


File 

-------------------------------

* The folder contains many files:
	* `nlp_project.ipynb` notebook containing the code used to analyse the corpus.
	* `clean_script.py` to clean the datasets.
	* `train_cuisine.csv` datasets before cleaning.
	* `output.csv` datasets after cleaning.
	* `recipes_raw_nosource_ar.json` dataset corpus to test final model.
	* `./core_solr/final_recipes_1.json` datasets recipes indexed to Solr platform.
	* `./core/final_recipe` contains all files used to obtain the platform.

Work Progress

-------------------------------

* Data Wrangling ( Clean data i.e Remove special character that add noise to our model )
* Text processing ( Using `NLTK toolkit` Cf. `nlp_project.ipynb` ) 
* Classifier Model ( Using `scikit-learn` and `pandas` )
	* Accuracy : `~75%`
* Using this classifier to predict `origin recipes` in a new corpus `recipes_raw_nosource_ar.json`.
* Indexing `./Recipe_prediction//final_recipes_1.json` in Solr.
* Parameter configuration of Solr platform to obtain : ![Alt text](/home/terjani/Images/Geography.png?raw=true "Interface Solr for information search")









