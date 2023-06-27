package com.example.myapplication.adaptador;

import android.content.Context;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.GridLayout;
import android.widget.GridView;
import android.widget.ImageView;

import com.example.myapplication.R;

public class FotosAdapter extends BaseAdapter {

    private Context mContext;
    public int[] imageArray = {
        R.drawable.aguila,
        R.drawable.conejo,
        R.drawable.gato,
        R.drawable.guacamaya,
        R.drawable.lobo,
        R.drawable.mariposa,
        R.drawable.oso,
        R.drawable.perro,
        R.drawable.tigre
    };

    public String descripcion(int position){
        String texto;
        switch (position){
            case 0:
                texto ="Aguila";
                break;
            case 1:
                texto ="Conejo";
                break;
            case 2:
                texto ="Gato";
                break;
            case 3:
                texto ="Guacamaya";
                break;
            case 4:
                texto ="Lobo";
                break;
            case 5:
                texto ="Mariposa";
                break;
            case 6:
                texto ="Oso";
                break;
            case 7:
                texto ="Perro";
                break;
            case 8:
                texto ="Tigre";
                break;
            default:
                throw new IllegalStateException("Unexpected value: " + position);
        }
        return texto;
    }

    public FotosAdapter(Context mContext) {
        this.mContext = mContext;
    }

    @Override
    public int getCount() {
        return imageArray.length;
    }

    @Override
    public Object getItem(int i) {
        return imageArray[i];
    }

    @Override
    public long getItemId(int i) {
        return 0;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        ImageView imageView = new ImageView(mContext);
        imageView.setImageResource(imageArray[position]);
        imageView.setScaleType(ImageView.ScaleType.CENTER_CROP);
        imageView.setLayoutParams(new GridView.LayoutParams(340, 350) );
        imageView.setContentDescription(descripcion(position));
        return imageView;
    }
}
