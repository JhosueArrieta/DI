package com.example.myothercatalog;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.ListAdapter;
import androidx.recyclerview.widget.RecyclerView;

import android.app.Activity;
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

    // Define adapters
    private ListAdapter listAdapter;  // Unused variable, can be removed
    private RecyclerView.Adapter adapter;  // Unused variable, can be removed

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize RecyclerView from the layout
        RecyclerView recyclerView = findViewById(R.id.RecyclerView);

        // Create an instance of the current activity
        Activity activity = this;

        // Create a JSON array request to fetch data from the given URL
        JsonArrayRequest request = new JsonArrayRequest(
                Request.Method.GET,
                "https://raw.githubusercontent.com/JhosueArrieta/DI/main/recursos/catalog.json",
                null,
                new Response.Listener<JSONArray>() {
                    @Override
                    public void onResponse(JSONArray response) {
                        // Create a list to store AnimalData objects
                        List<AnimalData> allTheAnimals = new ArrayList<>();

                        // Loop through the JSON array and create AnimalData objects
                        for (int i = 0; i < response.length(); i++) {
                            try {
                                JSONObject animal = response.getJSONObject(i);
                                AnimalData animals = new AnimalData(animal);
                                allTheAnimals.add(animals);
                            } catch (JSONException e) {
                                e.printStackTrace();
                            }
                        }

                        // Create an instance of the custom adapter and set it to the RecyclerView
                        AnimalRecyclerViewAdapter adapter = new AnimalRecyclerViewAdapter(allTheAnimals, activity);
                        recyclerView.setAdapter(adapter);
                        recyclerView.setLayoutManager(new LinearLayoutManager(activity));
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        // Handle errors and display a toast message
                        Toast.makeText(activity, error.getMessage(), Toast.LENGTH_SHORT).show();
                    }
                }
        );

        // Create a request queue and add the JSON array request to the queue
        RequestQueue cola = Volley.newRequestQueue(this);
        cola.add(request);
    }
}
