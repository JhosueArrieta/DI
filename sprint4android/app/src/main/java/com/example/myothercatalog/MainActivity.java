// MainActivity.java

package com.example.myothercatalog;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        RecyclerView recyclerView = findViewById(R.id.RecyclerView);
        Activity activity = this;

        JsonArrayRequest request = new JsonArrayRequest(
                Request.Method.GET,
                "https://raw.githubusercontent.com/JhosueArrieta/DI/main/recursos/catalog.json",
                null,
                new Response.Listener<JSONArray>() {
                    @Override
                    public void onResponse(JSONArray response) {
                        List<AnimalData> allTheAnimals = new ArrayList<>();
                        for (int i = 0; i < response.length(); i++) {
                            try {
                                JSONObject animal = response.getJSONObject(i);
                                AnimalData animals = new AnimalData(animal);
                                allTheAnimals.add(animals);
                            } catch (JSONException e) {
                                e.printStackTrace();
                            }
                        }

                        AnimalRecyclerViewAdapter adapter = new AnimalRecyclerViewAdapter(allTheAnimals, activity);
                        recyclerView.setAdapter(adapter);
                        recyclerView.setLayoutManager(new LinearLayoutManager(activity));

                        // Configurar el oyente de clics después de haber establecido el adaptador y el LayoutManager
                        adapter.setOnItemClickListener(new AnimalRecyclerViewAdapter.OnItemClickListener() {
                            @Override
                            public void onItemClick(int position) {
                                AnimalData clickedAnimal = allTheAnimals.get(position);
                                // Iniciar la nueva actividad
                                Intent intent = new Intent(MainActivity.this, DetailActivity.class);
                                // Puedes pasar datos adicionales a la nueva actividad si es necesario
                                // intent.putExtra("clave", valor);
                                startActivity(intent);
                            }
                        });
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        Toast.makeText(activity, error.getMessage(), Toast.LENGTH_SHORT).show();
                    }
                }
        );

        RequestQueue cola = Volley.newRequestQueue(this);
        cola.add(request);
    }
}
