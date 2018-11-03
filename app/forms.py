from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import BooleanField, SubmitField, StringField


class MethodSelectionForm(FlaskForm):
    # TODO: separate methods into divs by applicability
    # methods applied to initial data sets
    std_desc_stats = BooleanField("Standard Descriptive Stats", default=True)
    std_data_ranking = BooleanField("Standard Data Ranking", default=True)
    WGCNA = BooleanField("Weighted Correlation Network Analysis", default=True)
    std_cov = BooleanField("Standard Covariance", default=True)

    # methods applied to combined datasets, includes the above methods
    std_corr = BooleanField("Standard Correlation (Pearson)", default=True)
    spr_corr = BooleanField("Spearman Rank Correlation", default=True)
    kt_corr = BooleanField("Kendall Tau Correlation", default=True)

    # submit form
    submit = SubmitField("Analyze")


class DataUploadForm(FlaskForm):
    datafile = FileField(validators=[FileRequired(), FileAllowed(["xlsx"])])
    submit = SubmitField("Upload")


class CombinedForm(FlaskForm):
    datafile = FileField(validators=[FileRequired(), FileAllowed(["xlsx"])])
    job_name = StringField("Job Name")

    # TODO: separate methods into divs by applicability
    # methods applied to initial data sets
    std_desc_stats = BooleanField("Standard Descriptive Stats", default=True)
    std_data_ranking = BooleanField("Standard Data Ranking", default=True)
    WGCNA = BooleanField("Weighted Correlation Network Analysis", default=True)
    std_cov = BooleanField("Standard Covariance", default=True)

    # methods applied to combined datasets, includes the above methods
    std_corr = BooleanField("Standard Correlation (Pearson)", default=True)
    spr_corr = BooleanField("Spearman Rank Correlation", default=True)
    kt_corr = BooleanField("Kendall Tau Correlation", default=True)

    # methods added to test backgrounding
    delay_short = BooleanField("Add a 30-second delay", default=False)
    delay_long = BooleanField("Add a 5-minute delay", default=False)

    # submit form
    submit = SubmitField("Analyze")
