from django import forms
from django.forms import Form, ModelForm
from wishlist.models import BarangWishlist

class ItemForm(ModelForm):
    deskripsi = forms.CharField(max_length=200)
    class Meta:
        model = BarangWishlist
        fields = ['nama_barang', 'harga_barang', 'deskripsi']