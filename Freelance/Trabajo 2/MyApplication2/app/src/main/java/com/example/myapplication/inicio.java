package com.example.myapplication;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;

public class inicio extends AppCompatActivity {

    private Button btConversor,btImagenes;

    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.inicio_activity);

        btConversor = (Button) findViewById(R.id.btConversion);
        btImagenes = (Button) findViewById(R.id.btImagenes);

        btConversor.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(inicio.this, conversion.class);
                startActivity(intent);
            }
        });

        btImagenes.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(inicio.this, imagenes.class);
                startActivity(intent);
            }
        });

    }
}
