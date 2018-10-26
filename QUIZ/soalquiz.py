import shapefile										#Untuk mengambil data modul pada shapefile
w=shapefile.Writer()									#Untuk memasang fungsi writer
w.shapeType												#Untuk mengaktifkan type shape

w.field("kolom1","C")									#Untuk membuat kolom dengan menggunakan type data char
w.field("kolom2","C")

w.record("Line","satu")									#Kolom yang dibuat akan diisikan Recordnya sesuai dengan kolom yang ada
w.record("Line","satu")									

w.line(parts=[[[1,5],[5,5]]])							#Membuat koordinat berbentuk line/garis
w.line(parts=[[[6,9],[9,9]]])

w.save("soalquiz")									 	#Untuk menyimpan file menjadi file shp dengan nama file soal5.shp