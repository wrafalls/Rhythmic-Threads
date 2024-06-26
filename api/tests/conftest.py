import os
import shutil

import pytest

from app import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update(
        TESTING=True,
        SECRET_KEY="test",
        DATABASE=os.path.join(app.instance_path, "rt_test.sqlite"),
        SEED=True,
    )

    # init db
    with app.app_context():
        from app.db import setup_db

        setup_db()

        from app.sql.seed_products import seed_products

        seed_products(count=5)

    yield app

    # clean db
    shutil.rmtree(app.config["DATABASE"], ignore_errors=True)


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def cli(app):
    return app.test_cli_runner()
