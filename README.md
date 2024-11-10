# verizon_chatbot

## Objective

Customer service chatbot for Verizon utilizing the power of LLM (Claude by Anthropic) to summarize answers for user questions from the community.verizon.com. This will increase the ROI for Verizon, reduce the customer wait time for the answers and improve customer experience.

## Data input

Data is customer question (Prompt) and the Verizon private knoledgebase from community web site https://community.verizon.com/. Library webdriver is used to extract the multiple relevant information for lthe customer question from the verizon knoledgebase.

## Data cleanup

Utilizing Beautiful Soup to extract only the relevant text and specific links from the webdriver result (in HTML)

## Applying data model

Clude model "claude-3-sonnet-20240229" is used here for RAG.

## Enhancing the results

-

## Display the results

Provide a single accurate, most relevant and summarized answer for the user question. If it is not satisfactorily answer the user question then give specific instructions to post a question in Verizon community for community help or direct conact to Verizon customer service for further assistance.

## TODO

- Improve output presentaion
- In scraper.py/search_communitnse() input msg_title, snippet, url to results.append need fix.
