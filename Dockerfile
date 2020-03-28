FROM core_ml:version_2

WORKDIR /opt/

ADD models /opt/models

COPY models/requirements.txt ./
RUN pip install -r requirements.txt

RUN python3 -m zipfile -e /opt/egg/controller.egg ./temp_destination

RUN ls -l

EXPOSE 8000

CMD python -m models.LinearRegressionEstimator

