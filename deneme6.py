import tkinter as tk
from sklearn import tree
#tahmin etme kısmı x'e ağırlığı y'ye özellik atıyoruz. cf kısmı ise bir classification.Bir model.
def predict():
    x = int(weight_entry.get())
    y = int(feature_entry.get())

    pred = cf.predict([[x, y]])
#config yapılandırma dosyalarını okuyamak ve düzenlemek için.
    if (pred == 1):
        result_label.config(text='Portakal veya benzeri bir meyve olabilir.')
    elif (pred == 0):
        result_label.config(text='Elma veya benzeri bir meyve olabilir.')
    else:
        result_label.config(text='Geçersiz Tahmin')

root = tk.Tk()
root.title("Meyve Tahmin Etme")
#özellikler (ağırlık tahminine birkaç seçenek sunulmuş)
features = [[140, 1], [130, 1], [150, 0], [170, 0],
            [135, 1], [142, 1], [151, 1], [165, 0]]

labels = [0, 0, 1, 1, 0, 0, 0, 1]
#karar ağacı sınıflandırmayı kolaylaştırmak için. cf.fit ise koşullu durumlarla ilgili.
cf = tree.DecisionTreeClassifier()
cf = cf.fit(features, labels)

weight_label = tk.Label(root, text="Ağırlığı Girin:")
weight_label.grid(row=0, column=0)

weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1)

feature_label = tk.Label(root, text="Fiziksel Özellik Girin (Şekli düz, pürüzsüz ve sulu ise = 1, Şekli yumrulu ve pürüzlü ise = 0):")
feature_label.grid(row=1, column=0)

feature_entry = tk.Entry(root)
feature_entry.grid(row=1, column=1)

predict_button = tk.Button(root, text="Tahmin Et", command=predict)
predict_button.grid(row=2, column=0)

exit_button = tk.Button(root, text="Çıkış", command=root.quit)
exit_button.grid(row=2, column=1)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2)

root.mainloop()