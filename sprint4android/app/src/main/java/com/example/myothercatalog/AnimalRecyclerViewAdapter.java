package com.example.myothercatalog;

import android.app.Activity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class AnimalRecyclerViewAdapter extends RecyclerView.Adapter<AnimalViewHolder> {

    // Lista para almacenar los datos de los animales
    private List<AnimalData> alltheData;

    // Referencia a la actividad para manejar las interacciones
    private Activity activity;

    // Constructor para inicializar el adaptador con datos y actividad
    public AnimalRecyclerViewAdapter(List<AnimalData> dataSet, Activity activity) {
        this.alltheData = dataSet;
        this.activity = activity;
    }

    // Crea nuevas vistas (llamado por el administrador de diseño)
    @NonNull
    @Override
    public AnimalViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        // Infla el diseño animal_view_holder y crea un nuevo ViewHolder
        View view = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.animal_view_holder, parent, false);
        return new AnimalViewHolder(view);
    }

    // Reemplaza el contenido de una vista (llamado por el administrador de diseño)
    @Override
    public void onBindViewHolder(AnimalViewHolder holder, int position) {
        // Obtiene los datos para la posición dada y los vincula al ViewHolder
        AnimalData dataInPositionToBeRendered = alltheData.get(position);
        holder.showData(dataInPositionToBeRendered, activity);
    }

    // Devuelve el tamaño del conjunto de datos (llamado por el administrador de diseño)
    @Override
    public int getItemCount() {
        return alltheData.size();
    }
}
