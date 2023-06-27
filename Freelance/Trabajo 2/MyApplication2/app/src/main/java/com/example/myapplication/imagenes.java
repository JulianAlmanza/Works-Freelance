package com.example.myapplication;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.GridView;
import android.widget.ImageButton;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.example.myapplication.adaptador.FotosAdapter;

public class imagenes extends AppCompatActivity {

    GridView gridView;

    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.imagenes_activity);

        gridView = (GridView) findViewById(R.id.gv_imagenes);
        gridView.setAdapter(new FotosAdapter(this));

        gridView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
                Toast toast = Toast.makeText(imagenes.this, gridView.getAdapter().getView(i,view,adapterView).getContentDescription(),Toast.LENGTH_SHORT);
                toast.show();
            }
        });
    }

    public void  Regresar1(View view){
        Intent intent = new Intent(imagenes.this, inicio.class);
        startActivity(intent);
    }

}
