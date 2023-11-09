package com.example.mycatalog;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;

import androidx.annotation.Nullable;
import androidx.annotation.StringRes;
import androidx.fragment.app.Fragment;

public class CatalogFragment extends Fragment {
    private Button button; // Declaración de un botón como atributo
    private Context context; // Declaración de un contexto como atributo

    // Método estático para crear una nueva instancia de CatalogFragment con un ID de texto
    public static CatalogFragment newInstance(@StringRes int textId) {
        CatalogFragment fragment = new CatalogFragment();
        return fragment;
    }

    // Método que infla la interfaz de usuario del fragmento
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        // Inflar el fragmento utilizando el archivo XML correspondiente
        View layout = inflater.inflate(R.layout.catalog_fragment, container, false);
        button = layout.findViewById(R.id.buttonCF); // Asociar un botón por su ID

        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // Iniciar la actividad DetailActivity mediante un intent y startActivity
                Intent intentDetailActivity = new Intent(context, DetailActivity.class);
                startActivity(intentDetailActivity);
            }
        });

        return layout;
    }

    // Este método almacena el contexto del fragmento
    @Override
    public void onAttach(Context context) {
        super.onAttach(context);
        this.context = context;
    }
}