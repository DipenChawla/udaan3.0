### System Design Considerations

# Things to keep in mind
- Solutions ofering on-device processing is a plus.
- Processing time should not be more than 5 seconds.
- The model should be designed for a variety of image formats.

# Basic input of the system 
    - INPUT: An image
    - OUTPUT: dict(storename-str, store_address->str, dt->dtobject, invoice_no->str, total_amount->int, items = []) 

# Current stuff executed 

## Computer Vision
- Segmentation Model (text-detection-recognize-ctpn-tesseract)
- FAST-RCNN

## NLP:
- ORG and Address
- Product entity recogniton model
- Date Time Parser
- Total(REgex/ Cardinal)

- Fuzzy String Matching b/w predefined database OR 1:1 Mapping

# Aggregation
A final script will aggregate all the nlp outputs to and give the output(JSON)

# Things still unsure about:
- TXN number

# Server Config:
- EC2 p2 Instance(Probably Spot, or a dedicated one, Depending on the deployment)
- 

# Things to keep in mind
- Use async and multiprocess wherever required(e.g. Segmentation - Tesseract
                                                    TessOutput - NLP Modeling)