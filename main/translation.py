from modeltranslation.translator import register,TranslationOptions,translator
from .models import *


@register(feature)
class featureTranslationOptions(TranslationOptions):
    fields = ('name', 'text')

@register(text)
class textTranslationOptions(TranslationOptions):
    fields = ('text','nomi')


@register(sevice)
class seviceTranslationOptions(TranslationOptions):
    fields = ('name', 'text')

@register(work)
class workTranslationOptions(TranslationOptions):
    fields = ('name', 'text', 'title')

@register(plan)
class panTranslationOptions(TranslationOptions):
    fields = ('name', 'title1',  'title2', 'title3', 'title4', 'title5', 'title6', 'title7',)

@register(team2)
class team2TranslationOptions(TranslationOptions):
    fields = ('name', 'text', )

@register(team)
class teamTranslationOptions(TranslationOptions):
    fields = ('name', 'text', 'title',)

@register(answer)
class answerTranslationOptions(TranslationOptions):
    fields = ('name', 'text')

@register(questions)
class questionsTranslationOptions(TranslationOptions):
    fields = ('ism', 'e_mail', 'pro')

@register(by)
class byTranslationOptions(TranslationOptions):
    fields = ( 'text', 'name')

@register(our)
class ourTranslationOptions(TranslationOptions):
    fields = ('name', 'text')


