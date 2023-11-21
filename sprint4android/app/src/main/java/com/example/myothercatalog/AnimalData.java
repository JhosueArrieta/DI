package com.example.myothercatalog;

import org.json.JSONException;
import org.json.JSONObject;

public class AnimalData {
    private String name;
    private String description;
    private String image_url;
    public AnimalData(JSONObject json) {
        try {
            this.description =json.getString("description");
            this.name = json.getString("name");
            this.image_url = json.getString("image_url");
        }catch (JSONException e){
            e.printStackTrace();
        }
    }
    public String getName() {
        return name;
    }

    public String getDescription() {
        return description;
    }

    public String getImage_url() {
        return image_url;
    }


}
