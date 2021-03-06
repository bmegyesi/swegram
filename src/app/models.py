"""
model declaration of (
    UploadedFile,
    TextStats,
    Text,
    Paragraph,
    Sentence,
    Token
)
"""
from django.db import models


# This is used to check if an uploaded file has previously been annotated,
# if the md5 matches we can determine whether it's been normalized or not
class UploadedFile(models.Model):

    class Meta:
       app_label = 'app'
    
    md5_checksum = models.CharField(max_length=32, blank=False, primary_key=True)
    normalized = models.BooleanField(blank=False)


# class Text is a solution to solve the problem of selecting and update the activity of selected texts on real time
class TextStats(models.Model):
    
    class Meta:
        app_label = 'app'
    
    text_id      =   models.BigIntegerField(blank=True, null=True)
    activated    =   models.BooleanField(default=False)
    date_added   =   models.DateTimeField(auto_now_add=True)

    lang         =   models.CharField(max_length=512)
    filename     =   models.CharField(max_length=512)
    file_size    =   models.CharField(max_length=512)
    normalized   =   models.BooleanField(default=False)
    parsed       =   models.BooleanField(default=False)
    has_label    =   models.BooleanField(default=False)
    labels       =   models.TextField(null=True)
 
    number_of_paragraphs = models.IntegerField(blank=True, null=True)
    number_of_sentences  = models.IntegerField(blank=True, null=True)

    def __repr__(self):
        return self.filename
     

class Text(models.Model):

    class Meta:
        app_label = 'app'

    stats               = models.OneToOneField(TextStats, on_delete=models.CASCADE)

    general             = models.TextField(null=True)
    readability         = models.TextField(null=True)
    morph               = models.TextField(null=True)
    morph_average       = models.TextField(null=True)
    lexical             = models.TextField(null=True)
    lexical_average     = models.TextField(null=True)
    syntactic           = models.TextField(null=True)
    syntactic_average   = models.TextField(null=True)
    content             = models.TextField(null=True) 


    def __str__(self):
        return self.content


class Paragraph(models.Model):

    class Meta:
        app_label = 'app'

    text = models.ForeignKey(Text, on_delete=models.CASCADE)

    general             = models.TextField(null=True)
    readability         = models.TextField(null=True)
    morph               = models.TextField(null=True)
    morph_average       = models.TextField(null=True)
    lexical             = models.TextField(null=True)
    lexical_average     = models.TextField(null=True)
    syntactic           = models.TextField(null=True)
    syntactic_average   = models.TextField(null=True)
    
    content             = models.TextField(null=True)

    def __str__(self):
        return self.content

class Sentence(models.Model):

    class Meta:
        app_label = 'swegram_main'
    
    text        = models.ForeignKey(Text, on_delete=models.CASCADE)
    paragraph   = models.ForeignKey(Paragraph, on_delete=models.CASCADE)
    
    text_index  = models.CharField(max_length=512)
    types       = models.TextField(null=True)
    ud_tree     = models.BooleanField(default=True)

    general     = models.TextField(null=True)
    readability = models.TextField(null=True) 
    morph       = models.TextField(null=True) 
    lexical     = models.TextField(null=True)
    syntactic   = models.TextField(null=True)
    
    content     = models.TextField(null=True)
    
    def __str__(self):
        return self.content


class Token(models.Model):
    
    class Meta:
        app_label = 'swegram_main'
    
    sentence = models.ForeignKey(Sentence, on_delete=models.CASCADE)
  
    compound_originals   = models.BooleanField(default=False)
    normalized           = models.BooleanField(default=False)
    token_index          = models.CharField(max_length=512)
    text_index           = models.CharField(max_length=512)
    form                 = models.CharField(max_length=512, default="_")
    norm                 = models.CharField(max_length=512, default="_", blank=True)
    lemma                = models.CharField(max_length=512, default="_", blank=True)
    upos                 = models.CharField(max_length=512, default="_", blank=True)
    xpos                 = models.CharField(max_length=512, default="_", blank=True) 
    feats                = models.CharField(max_length=512, default="_", blank=True) 
    ufeats               = models.CharField(max_length=512, default="_", blank=True) 
    head                 = models.CharField(max_length=512, default="_", blank=True) 
    deprel               = models.CharField(max_length=512, default="_", blank=True) 
    deps                 = models.CharField(max_length=512, default="_", blank=True) 
    misc                 = models.CharField(max_length=512, default="_", blank=True) 
    path                 = models.CharField(max_length=512, default="", blank=True)
    highlight            = models.CharField(max_length=512, default="", blank=True)
    length               = models.IntegerField(blank=True, null=True) 
    dep_length           = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.form
