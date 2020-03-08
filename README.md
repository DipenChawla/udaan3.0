# U-DAAN 3.0
Udaan3.0 - Our implementation of extraction of data from invoices of food and fashion brands.


Hey there! Follow this guide for a short intro to the architecture and overview of our text extraction and classification system.

The basic architecture of our system is divided into three parts
* Invoice upload system
* Semantic extraction of text with pytesseract
* Validation of extracted text with BERT and a host of other techniques.


The architecture is summarised in the diagram below.

![Architecture](https://github.com/DipenChawla/udaan3.0/blob/master/img/architecture.png)

There are two different EC2 servers hosting their own services, that is computer vision and natural text processes correspondingly. 

The two servers are connected with the help of a common message broker, RabbitMQ allowing the text processes to access the input text fields in an instant. This also decouples both the services effectively allowing them to execute their tasks in a decoupled environment.
This also provides the opportunity to allow for the scaling of the two services depending upon the load.

We understand that the system is in no way perfect, and has a lot of scope for improvement. One of them is to parallelize the tesseract module to achieve faster runtimes and optimum queue scheduling.

We would love to hear more about your feedback, let us know if you have any queries. FIN.