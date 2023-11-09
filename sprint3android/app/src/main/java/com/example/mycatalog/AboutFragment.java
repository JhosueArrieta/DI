package com.example.mycatalog;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.Nullable;
import androidx.annotation.StringRes;
import androidx.fragment.app.Fragment;

public class AboutFragment extends Fragment {
    // Método estático para crear una nueva instancia de AboutFragment con un ID de texto
    public static AboutFragment newInstance(@StringRes int textId) {
        AboutFragment fragment = new AboutFragment();
        return fragment;
    }

    // Método que infla la interfaz de usuario del fragmento
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        // Inflar el fragmento utilizando el archivo XML correspondiente
        View layout = inflater.inflate(R.layout.about_fragment, container, false);

        return layout;
    }
}
