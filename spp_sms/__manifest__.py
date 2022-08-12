# Part of OpenSPP. See LICENSE file for full copyright and licensing details.


{
    "name": "OpenSPP SMS",
    "category": "OpenSPP",
    "version": "15.0.0.0.2",
    "sequence": 1,
    "author": "OpenSPP.org",
    "website": "https://openspp.org/",
    "license": "AGPL-3",
    "depends": ["iap", "sms", "mass_mailing_sms", "g2p_registry_base", "g2p_programs"],
    "external_dependencies": {
        "python": [
            "twilio.rest",
            "boto3",
        ]
    },
    "data": [
        "views/iap_account_view.xml",
        "views/mailing_mailing.xml",
        "security/ir.model.access.csv",
    ],
    "assets": {},
    "demo": [],
    "images": [],
    "application": True,
    "installable": True,
    "auto_install": False,
}
