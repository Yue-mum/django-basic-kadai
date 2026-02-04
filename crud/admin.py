#管理者画面をカスタマイズするためのコード

#contribとは、Djangoが提供する追加機能の集まりを指します。adminはその中の管理者画面に関する機能です。
from django.contrib import admin
#models.pyに定義されたデータベースのモデルをインポートします。
from .models import Product
# Register your models here.


#管理者画面でProductモデルをどのように表示・操作するかを定義するクラスです。
#ModelAdminは、Djangoの管理者画面でモデルを管理するための基本クラスです。ModelAdminをProductAdminクラスで継承しています。
#継承とは、既存のクラスの機能を引き継ぎつつ、新たな機能を追加したり、既存の機能を変更したりすることを指します。
class ProductAdmin(admin.ModelAdmin):
    #list_display属性は、管理者画面の一覧表示で表示するフィールドを指定します。ここでは'id', 'name', 'price'の3つのフィールドを表示します。
    list_display = ('id', 'name', 'price')
    #search_fields属性は、管理者画面の検索ボックスで検索対象とするフィールドを指定します。ここでは'name'フィールドを検索対象としています。
    search_fields = ('name',)
# admin.site.registerは、管理者画面にモデルを登録するための関数です。ここではProductモデルをProductAdminクラスの設定で登録しています。
admin.site.register(Product, ProductAdmin)