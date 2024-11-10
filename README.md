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

## Setup

## Run command

curl --location 'http://127.0.0.1:8000/chat' \
--header 'Content-Type: application/json' \
--data '{"text": "Iphone 16 pro shipping delay fixed"}'

## TODO

- Improve output presentaion
- In scraper.py/search_communitnse() input msg_title, snippet, url to results.append need fix.
- How setup and run the project

## soup

<div class="lia-quilt lia-quilt-message-search-item lia-quilt-layout-list-item">
                                            <div class="lia-quilt-row lia-quilt-row-top">
                                              <div class="lia-quilt-column lia-quilt-column-18 lia-quilt-column-left lia-quilt-column-left-content">
                                                <div class="lia-quilt-column-alley lia-quilt-column-alley-left">
                                                  <div class="UserAvatar lia-user-avatar lia-component-common-widget-user-avatar lia-component-message-view-widget-author-avatar">
                                                    <img alt="polakowski1" class="lia-user-avatar-message" data-airgap-id="20" id="imagedisplay" src="/t5/image/serverpage/avatar-name/Road/avatar-theme/candy/avatar-collection/Verizon_Core/avatar-display-size/message/version/2?xdesc=1.0" title="polakowski1">
                                                  </div>
                                                  <div class="lia-message-subject-wrapper lia-component-subject lia-component-message-view-widget-subject-with-options">
                                                    <div class="MessageSubject">
                                                      <div class="MessageSubjectIcons">
                                                        <div class="message-subject" itemprop="name">
                                                          <span class="lia-message-unread lia-message-unread-windows">
                                                            <a class="page-link lia-link-navigation lia-custom-event" href="/t5/Order-Tracking/Iphone-16-pro-shipping-delay-fixed/m-p/1786795?search-action-id=218717103662&amp;search-result-uid=1786795" id="link_3">
                                                              <span class="lia-search-match-lithium">Iphone</span>
                                                              <span class="lia-search-match-lithium">16</span>
                                                              <span class="lia-search-match-lithium">pro</span>
                                                              <span class="lia-search-match-lithium">shipping</span>
                                                              <span class="lia-search-match-lithium">delay</span>
                                                              <span class="lia-search-match-lithium">fixed</span>
                                                            </a>
                                                          </span>
                                                        </div>
                                                      </div>
                                                    </div>
                                                  </div>
                                                  <span class="lia-message-byline lia-message-byline-author-rank-board-date-unread lia-component-message-view-widget-byline-author-rank-board-date-unread">
                                                    <span class="lia-byline-item">By
                                                      <span class="UserName lia-user-name lia-user-rank-Newbie lia-component-users-widget-user-name">
                                                        <a aria-haspopup="true" aria-label="View Profile of polakowski1" class="lia-link-navigation lia-page-link lia-user-name-link" href="https://community.verizon.com/t5/user/viewprofilepage/user-id/5578721" id="link_1f168c5b35ad30" itemprop="url" style="color: #747676" target="_self"><span class="">polakowski1</span></a>
                                                      </span></span><span class="lia-byline-item">Newbie</span><span class="lia-byline-item"><i aria-label="forum" class="lia-img-icon-forum-board lia-fa-icon lia-fa-forum lia-fa-board lia-fa" role="img" title="forum"></i><a class="lia-link-navigation lia-message-board-link lia-component-common-widget-link" href="/t5/Order-Tracking/bd-p/mobile-order-tracking" id="link_1f168c5b76df35">Order &amp; Tracking</a></span><span class="lia-byline-item"><span class="DateTime lia-component-common-widget-date">
                                                        <span class="local-date">‎11-08-2024</span>
                                                        <span class="local-time">04:24 PM</span>
                                                      </span></span>
                                                  </span>
                                                </div>
                                              </div>
                                              <div class="lia-quilt-column lia-quilt-column-06 lia-quilt-column-right lia-quilt-column-right-content lia-mark-empty"></div>
                                            </div>
                                            <div class="lia-quilt-row lia-quilt-row-contents">
                                              <div class="lia-quilt-column lia-quilt-column-24 lia-quilt-column-single lia-quilt-column-full-content">
                                                <div class="lia-quilt-column-alley lia-quilt-column-alley-single">
                                                  <div class="lia-message-body-wrapper lia-component-message-view-widget-body">
                                                    <div class="lia-message-body" id="bodyDisplay" itemprop="text">
                                                      <div class="lia-message-body-content">
                                                        <div class="lia-truncated-body-container">
                                                          I ordered an
                                                          <span class="lia-search-match-lithium lia-search-match-lithium">iphone</span>
                                                          <span class="lia-search-match-lithium lia-search-match-lithium">16</span>
                                                          <span class="lia-search-match-lithium lia-search-match-lithium">pro</span>
                                                          on 10/11. It said it
                                                          would
                                                          <span class="lia-search-match-lithium lia-search-match-lithium">ship</span>
                                                          on 10/11. &nbsp;Not so. I
                                                          have wasted too much
                                                          time with Verizon
                                                          support regarding a
                                                          <span class="lia-search-match-lithium lia-search-match-lithium">ship</span>
                                                          date. The chat bots
                                                          are a joke and want
                                                          you to b...
                                                        </div>
                                                      </div>
                                                    </div>
                                                  </div>
                                                </div>
                                              </div>
                                            </div>
                                          </div>

URL
<a class="page-link lia-link-navigation lia-custom-event" href="/t5/Order-Tracking/Iphone-16-pro-shipping-delay-fixed/m-p/1786795?search-action-id=218717103662&amp;search-result-uid=1786795" id="link_3">

TITLE
<span class="lia-search-match-lithium">Iphone</span>
<span class="lia-search-match-lithium">16</span>
<span class="lia-search-match-lithium">pro</span>
<span class="lia-search-match-lithium">shipping</span>
<span class="lia-search-match-lithium">delay</span>
<span class="lia-search-match-lithium">fixed</span>
</a>

SNIPPET

<div class="lia-message-body-content">
<div class="lia-truncated-body-container">
I ordered an
<span class="lia-search-match-lithium lia-search-match-lithium">iphone</span>
<span class="lia-search-match-lithium lia-search-match-lithium">16</span>
<span class="lia-search-match-lithium lia-search-match-lithium">pro</span>
on 10/11. It said it
would
<span class="lia-search-match-lithium lia-search-match-lithium">ship</span>
on 10/11. &nbsp;Not so. I
have wasted too much
time with Verizon
support regarding a
<span class="lia-search-match-lithium lia-search-match-lithium">ship</span>
date. The chat bots
are a joke and want
you to b...
</div>
</div>

=================================

**\_** START TITLE \***\*\_\*\***
[{'title': 'Iphone 16 pro shipping delay fixed', 'snippet': 'I ordered an iphone 16 pro on 10/11. It said it would ship on 10/11. \xa0Not so. I have wasted too much time with Verizon support regarding a ship date. The chat bots are a joke and want you to b...', 'url': 'https://community.verizon.com/t5/Order-Tracking/Iphone-16-pro-shipping-delay-fixed/m-p/1786795'},

{'title': 'iPhone 16 16 Pro 16 Pro', 'snippet': '...won’t ship until 10/11? \xa0This makes no sense at all. \xa0 At a minimum, Verizon should be shipping the iphone 16 when it becomes available, even if 16 pro or 16 pro max may not be available....', 'url': 'https://community.verizon.com/t5/Apple/Delayed-iPhone-16-16-Pro-and-16-Pro-Max/m-p/1779100'},

"Based on the following Verizon Community information, please answer the user's question.\n If you can't find a relevant answer in the provided context, say so and suggest contacting Verizon support directly.\n\n User Question: Iphone 16 pro shipping delay fixed\n\n Verizon Community Information:\n Title: Iphone 16 pro shipping delay fixed\nContent: I ordered an iphone 16 pro on 10/11. It said it would ship on 10/11. \xa0Not so. I have wasted too much time with Verizon support regarding a ship date. The chat bots are a joke and want you to b...\nURL: https://community.verizon.com/t5/Order-Tracking/Iphone-16-pro-shipping-delay-fixed/m-p/1786795\n\nTitle: iPhone 16 16 Pro 16 Pro\nContent: ...won’t ship until 10/11? \xa0This makes no sense at all. \xa0 At a minimum, Verizon should be shipping the iphone 16 when it becomes available, even if 16 pro or 16 pro max may not be available....\nURL: https://community.verizon.com/t5/Apple/Delayed-iPhone-16-16-Pro-and-16-Pro-Max/m-p/1779100\n\nTitle: iphone 16 pro\nContent: Hi,\xa0 \n I've been a LOYAL customer to Verizon for over a decade - probably longer if I go look.... i'm too frustrated to do that. I ordered an iPhone 16 Pro Max on 9-16. This order had a shipping...\nURL: https://community.verizon.com/t5/Apple/iphone-16-pro-max/m-p/1782148"
