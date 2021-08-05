class QA_Router:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'QA':
            return 'db_QA'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'QA':
            return 'db_QA'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'QA' or \
            obj2._meta.app_label == 'QA':
            return True

    def allow_migrate(self, db, app_label, model=None, **hints):
        if app_label == 'QA':
            return db == 'db_QA'