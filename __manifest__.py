# -*- coding: utf-8 -*-
{
    "name": "My Bank (G1 Bank)",
    "summary": "Gestión bancaria en Odoo: cuentas, movimientos y clientes.",
    "description": """
        Módulo de gestión bancaria para Odoo 16.
        Permite gestionar cuentas (estándar y de crédito), registrar
        movimientos (depósitos y pagos) con recálculo automático de balance
        y validaciones, y consultar los clientes (basados en res.users).
    """,
    "author": "daaniidam",
    "website": "https://github.com/daaniidam/g1_bank",
    "category": "Finance",
    "version": "16.0.1.0.0",
    "license": "MIT",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/views.xml",
        "views/g1_bank_customer.xml",
    ],
    "application": True,
    "installable": True,
}
