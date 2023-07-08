# Generated by Django 4.2.1 on 2023-07-08 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    replaces = [
        ("spid_cie_oidc_entity", "0021_federationhistoricalkey"),
        ("spid_cie_oidc_entity", "0022_federationhistoricalkey_jwk_and_more"),
        ("spid_cie_oidc_entity", "0023_alter_federationhistoricalkey_jwk"),
        ("spid_cie_oidc_entity", "0024_alter_federationhistoricalkey_kid"),
        ("spid_cie_oidc_entity", "0025_alter_federationhistoricalkey_jwk"),
        ("spid_cie_oidc_entity", "0026_alter_federationhistoricalkey_jwk"),
    ]

    dependencies = [
        (
            "spid_cie_oidc_entity",
            "0020_alter_federationentityconfiguration_jwks_core_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="FederationHistoricalKey",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("kid", models.CharField(max_length=128)),
                (
                    "inactive_from",
                    models.DateTimeField(
                        help_text="Expired or Revocation date if revocation motivation is configured"
                    ),
                ),
                (
                    "revocation_motivation",
                    models.CharField(
                        blank=True,
                        choices=[
                            (0, "unspecified"),
                            (1, "keyCompromise"),
                            (2, "cACompromise"),
                            (3, "affiliationChanged"),
                            (4, "superseded"),
                            (5, "cessationOfOperation"),
                            (6, "certificateHold"),
                            (8, "removeFromCRL"),
                            (9, "privilegeWithdrawn"),
                            (10, "aACompromise"),
                        ],
                        max_length=33,
                    ),
                ),
                (
                    "entity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="spid_cie_oidc_entity.federationentityconfiguration",
                    ),
                ),
                ("jwk", models.JSONField(default=dict, help_text="private jwk")),
            ],
            options={
                "verbose_name": "Federation Historical Key",
                "verbose_name_plural": "Federation Historical Keys",
            },
        ),
    ]
