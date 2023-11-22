// DetailActivity.java
package com.example.myothercatalog;

import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.bumptech.glide.Glide;

public class DetailActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);

        // Obtener la información del animal del intent
        AnimalData animal = getIntent().getParcelableExtra("animal");

        // Referencias a los elementos de la interfaz de usuario en activity_detail.xml
        ImageView imageView = findViewById(R.id.imageView);
        TextView textTitle = findViewById(R.id.textTitle);
        TextView textDescription = findViewById(R.id.textDescription);

        // Mostrar la información del animal en la interfaz de usuario
        textTitle.setText(animal.getName());
        textDescription.setText(animal.getDescription());

        // Utilizar Glide para cargar la imagen desde la URL y mostrarla en el ImageView
        Glide.with(this)
                .load(animal.getImage_url())
                .into(imageView);
    }
}
