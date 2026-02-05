# views.pyでは、各URLに対応する処理（ビュー）を定義します。

#shortcut関数は、よく使うDjangoの機能を簡単に使えるようにするためのものです。
# renderは、テンプレートを使ってHTMLを生成するための関数です。
from django.shortcuts import render
# .views.genericには、Djangoが提供する汎用的なビュークラスが含まれています。例えば、TemplateViewはテンプレートを表示するためのビュークラスです。
from django.views.generic import TemplateView, ListView, DetailView
#.editには、データの作成、更新、削除を行うための汎用的なビュークラスが含まれています。
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# .modelsはmodels.pyに定義されたデータベースのモデルをインポートします。
from .models import Product
#.urlsには、URLの逆引きを行うための関数が含まれています。逆引きとは、URLの名前から実際のURLパスを取得することです。
# reverse_lazyは、URLの逆引きを遅延評価するための関数です。これは、ビュークラスの属性として使用する場合に便利です。
from django.urls import reverse_lazy

# TemplateViewは、指定されたテンプレートを表示するためのビュークラスです。ここではtop.htmlテンプレートを表示します。
class TopView(TemplateView):
    template_name = "top.html"

#ListViewは、データベースのオブジェクトのリストを表示するためのビュークラスです。
# オブジェクトとは、データベースに保存されている各レコード（行）のことを指します。
class ProductListView(ListView):
    model = Product
    # paginate_by属性は、1ページあたりに表示するオブジェクトの数を指定します。ここでは3件ずつ表示します。
    paginate_by = 1

# CreateViewは、新しいオブジェクトを作成するためのビュークラスです。ここではProductモデルの新しいインスタンスを作成します。
# インスタンスとは、モデルの具体的なデータを持つオブジェクトのことを指します。たとえば、Productモデルのインスタンスは、特定の商品（名前や価格などの属性を持つ）を表します。
class ProductCreateView(CreateView):
    model = Product
    # fields属性は、フォームに表示するモデルのフィールドを指定します。'__all__'はすべてのフィールドを表示することを意味します。
    # フィールドとは、モデルの属性（例えばnameやpriceなど）を指します。
    fields = '__all__'

#UpdateViewは、既存のオブジェクトを更新するためのビュークラスです。ここではProductモデルのインスタンスを更新します。
class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    #temoplate_name_suffix属性は、使用するテンプレートの名前のサフィックスを指定します。デフォルトでは'_form'ですが、ここでは'_update_form'に変更しています。
    #サックスとは、ファイル名の末尾に付け加えられる部分のことです。例えば、'product_update_form.html'のようになります。
    template_name_suffix = '_update_form'

# DeleteViewは、既存のオブジェクトを削除するためのビュークラスです。ここではProductモデルのインスタンスを削除します。
class ProductDeleteView(DeleteView):
    model = Product
    #success_url属性は、削除が成功した後にリダイレクトするURLを指定します。ここでは'reverse_lazy'を使って'list'という名前のURLにリダイレクトします。
    #リダイレクトとは、あるURLから別のURLに自動的に移動することを指します。
    success_url = reverse_lazy('list')

#DetailViewは、特定のオブジェクトの詳細情報を表示するためのビュークラスです。ここではProductモデルのインスタンスの詳細を表示します。
class ProductDetailView(DetailView):
    model = Product