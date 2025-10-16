from django.contrib import admin
from django.utils.html import format_html
from .models import JadwalMisa
from .models import Berita, Kategori

@admin.register(JadwalMisa)
class JadwalMisaAdmin(admin.ModelAdmin):
    list_display = ('nama_misa', 'hari', 'waktu', 'tampilkan_gambar')
    list_filter = ('hari',)
    search_fields = ('nama_misa',)
    ordering = ('hari', 'waktu')

    def tampilkan_gambar(self, obj):
        if obj.gambar:
            return format_html(
                '<img src="{}" width="70" height="70" style="object-fit: cover; border-radius: 8px;" />',
                obj.gambar.url
            )
        return "Tidak ada gambar"
    tampilkan_gambar.short_description = "Gambar"

@admin.register(Kategori)
class KategoriAdmin(admin.ModelAdmin):
    list_display = ('nama',)
    prepopulated_fields = {'slug': ('nama',)}

@admin.register(Berita)
class BeritaAdmin(admin.ModelAdmin):
    list_display = ('judul', 'kategori', 'tanggal', 'penulis')
    list_filter = ('kategori', 'tanggal')
    search_fields = ('judul', 'isi')
    prepopulated_fields = {'slug': ('judul',)}
