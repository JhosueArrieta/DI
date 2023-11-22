package com.example.myothercatalog;

import android.os.Parcel;
import android.os.Parcelable;

import org.json.JSONException;
import org.json.JSONObject;

public class AnimalData implements Parcelable {
    private String name;
    private String description;
    private String image_url;

    public AnimalData(JSONObject json) {
        try {
            this.description = json.getString("description");
            this.name = json.getString("name");
            this.image_url = json.getString("image_url");
        } catch (JSONException e) {
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

    // Implementación de Parcelable

    protected AnimalData(Parcel in) {
        name = in.readString();
        description = in.readString();
        image_url = in.readString();
    }

    public static final Creator<AnimalData> CREATOR = new Creator<AnimalData>() {
        @Override
        public AnimalData createFromParcel(Parcel in) {
            return new AnimalData(in);
        }

        @Override
        public AnimalData[] newArray(int size) {
            return new AnimalData[size];
        }
    };

    @Override
    public int describeContents() {
        return 0;
    }

    @Override
    public void writeToParcel(Parcel dest, int flags) {
        dest.writeString(name);
        dest.writeString(description);
        dest.writeString(image_url);
    }
}
