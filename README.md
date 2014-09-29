img2plus
========

Automatic image to google plus sync

The problem is that while there are great tools to store your images (e.g. Owncloud) there are no really good online viewers (especially for your mobiles) available. So the idea is to store the images in your owncloud and regularly check for new images and upload them in an reduced size (the g+ free )k pixl limit) to your private google plus account. Since I want to share the images with multiple accounts it should be possible to upload the folder to multiple accounts. The tool should not only upload the images but really keep them in sync with the Owncloud being the master.

Requirements
===============
To run img2plus you require the following dependencies on your path:

* python2

* httplib
* urlparse
* [oauth2client](https://code.google.com/p/google-api-python-client/wiki/OAuth2Client)

Secrets
========
As a project which requires to upload images in the background on a headless server to google plus we need to use their security mechanism. Therefore the img2plus.p12 and img2plus.json file need to be downloaded and put into the root folder of this project. Those files are ignored and will not be uploaded.

