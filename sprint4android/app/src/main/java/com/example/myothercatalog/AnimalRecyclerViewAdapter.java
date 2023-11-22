// AnimalRecyclerViewAdapter.java

package com.example.myothercatalog;

import android.app.Activity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class AnimalRecyclerViewAdapter extends RecyclerView.Adapter<AnimalViewHolder> {

    private List<AnimalData> alltheData;
    private Activity activity;
    private OnItemClickListener mListener;

    public interface OnItemClickListener {
        void onItemClick(int position);
    }

    public void setOnItemClickListener(OnItemClickListener listener) {
        mListener = listener;
    }

    public AnimalRecyclerViewAdapter(List<AnimalData> dataSet, Activity activity) {
        this.alltheData = dataSet;
        this.activity = activity;
    }

    @NonNull
    @Override
    public AnimalViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.animal_view_holder, parent, false);
        return new AnimalViewHolder(view);
    }

    @Override
    public void onBindViewHolder(AnimalViewHolder holder, int position) {
        AnimalData dataInPositionToBeRendered = alltheData.get(position);
        holder.showData(dataInPositionToBeRendered, activity);

        final int adapterPosition = holder.getAdapterPosition();

        holder.itemView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (mListener != null && adapterPosition != RecyclerView.NO_POSITION) {
                    mListener.onItemClick(adapterPosition);
                }
            }
        });
    }
    @Override
    public int getItemCount() {
        return alltheData.size();
    }
}
