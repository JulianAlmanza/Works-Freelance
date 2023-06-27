package com.example.myapplication;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.RadioButton;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class conversion extends AppCompatActivity {

    private EditText edtDato;
    private TextView tvVConversion,tvConversion;
    private RadioButton rbtnDolares, rbtnEuros;

    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.conversion_activity);

        edtDato = (EditText) findViewById(R.id.edtDato);
        tvConversion = (TextView) findViewById(R.id.tvConversion);
        tvVConversion = (TextView) findViewById(R.id.tvVConversion);
        rbtnDolares = (RadioButton) findViewById(R.id.rbtnDolares);
        rbtnEuros = (RadioButton) findViewById(R.id.rbtnEuros);
    }

    public void  Regresar(View view){
        Intent intent = new Intent(conversion.this, inicio.class);
        startActivity(intent);
    }

    public void Operar(View view) {

        if (edtDato.getText().toString().isEmpty()) {
            edtDato.setError("Debe digitar un numero de Pesos Colombianos a convertir");
        } else {
            String valor1 = edtDato.getText().toString();
            int nro1 = Integer.parseInt(valor1);
            if (rbtnDolares.isChecked()) {
                tvVConversion.setText("CONVERSION (Peso COL -> Dolar USD)");
                double resul = nro1 * 0.00023;
                String conver = String.valueOf(resul);
                tvConversion.setText(conver);
            } else if (rbtnEuros.isChecked()) {
                tvVConversion.setText("CONVERSION (Peso COL -> Euro EUR)");
                double resul = nro1 * 0.000228;
                String conver = String.valueOf(resul);
                tvConversion.setText(conver);
            }else{
                rbtnDolares.setError("Debe Selecionar una Opcion para poder convertir");
                tvConversion.setText("¡Ojo...Debe Selecionar una opcion para poder Convertir!");
            }
        }
    }
}
