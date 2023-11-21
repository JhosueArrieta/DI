package com.example.myothercatalog;

import android.app.Activity;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;

public class AnimalViewHolder extends RecyclerView.ViewHolder {

    // Elementos de la interfaz de usuario en el ViewHolder
    private final TextView textView;
    private final ImageView imageView;

    // Constructor que toma una vista como parámetro (representa un elemento de la lista)
    public AnimalViewHolder(@NonNull View itemView) {
        super(itemView);

        // Inicializa los elementos de la interfaz de usuario con los identificadores definidos en el diseño
        textView = (TextView) itemView.findViewById(R.id.animal_text_view);
        imageView = (ImageView) itemView.findViewById(R.id.animal_image_view);
    }

    // Método para mostrar los datos en el ViewHolder
    public void showData(AnimalData data, Activity activity) {
        // Establece el texto del TextView con el nombre del animal
        textView.setText(data.getName());

        // Utiliza la biblioteca Glide para cargar la imagen desde la URL y mostrarla en el ImageView
        Glide.with(itemView.getContext())
                .load(data.getImage_url())
                .into(imageView);
    }
}
