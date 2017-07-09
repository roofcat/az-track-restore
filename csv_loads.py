# encoding:utf-8


import json
import date_utils


CSV_SUCCESS = "success.csv"
CSV_ERRORS = "errors.csv"

CSV_HEADER_ERROR = [
    'event', 'correo', 'timestamp', 'sg_message_id', 'sg_event_id', 'smtp_id',
    'ip', 'useragent', 'response', 'reason', 'status', 'type', 'url'
]

CSV_HEADER_SUCCESS = [
    'input_date', 'empresa_id', 'rut_receptor', 'rut_emisor', 'tipo_envio',
    'tipo_dte_id', 'numero_folio', 'resolucion_receptor', 'resolucion_emisor',
    'monto', 'fecha_emision', 'fecha_recepcion', 'estado_documento',
    'tipo_operacion', 'tipo_receptor', 'id_envio', 'nombre_cliente', 'correo',
    'smtp_id', 'processed_date', 'processed_event', 'processed_sg_event_id',
    'processed_sg_message_id', 'delivered_date', 'delivered_event',
    'delivered_sg_event_id', 'delivered_sg_message_id', 'delivered_response',
    'opened_first_date', 'opened_last_date', 'opened_event', 'opened_ip',
    'opened_user_agent', 'opened_sg_event_id', 'opened_sg_message_id',
    'opened_count', 'dropped_date', 'dropped_sg_event_id',
    'dropped_sg_message_id', 'dropped_reason', 'dropped_event', 'bounce_date',
    'bounce_event', 'bounce_sg_event_id', 'bounce_sg_message_id',
    'bounce_reason', 'bounce_status', 'bounce_type', 'unsubscribe_date',
    'unsubscribe_uid', 'unsubscribe_purchase', 'unsubscribe_id',
    'unsubscribe_event', 'click_ip', 'click_purchase', 'click_useragent',
    'click_event', 'click_email', 'click_date', 'click_url'
]


def exist_trunc(row):
    print "Validando existencia de trunc"
    try:
        val = row['trunc']
        if val:
            return True
        else:
            return False
    except Exception as e:
        print e
        return False


def get_row_field(obj, pos):
    print "Obteniendo row field: " + str(pos)
    if obj is not None:
        try:
            return '"' + obj[pos] + '"'
        except Exception:
            return ''


def get_field(obj, field):
    print "Convirtiendo " + field
    if obj is not None:
        try:
            return '"' + str(obj[field]) + '"'
        except Exception:
            return ''
    else:
        return ''


def get_header(header):
    print "get_header "
    linea = ""
    for h in header:
        linea += '"' + str(h) + '",'
    linea = linea[:-1]
    return linea + "\n"


def crear_linea_csv(header, row):
    print "crear_linea_csv " + str(row)
    linea = ""
    for h in header:
        try:
            linea += str(row[h]) + ","
        except Exception as e:
            print e
            linea += str("") + ','
    linea = linea[:-1]
    print linea + "\n"
    return linea + "\n"


def generar_csv(reader):
    csv_success = open(CSV_SUCCESS, "w")
    csv_success.write(get_header(CSV_HEADER_SUCCESS))
    csv_errors = open(CSV_ERRORS, "w")
    csv_errors.write(get_header(CSV_HEADER_ERROR))
    print "Cabeceras creadas"
    row = dict()
    if reader is not None:
        for data in reader:
            if data[0] == 'event':
                print data
            else:
                print data
                try:

                    if data[13]:
                        j = json.loads(data[13])

                        if exist_trunc(j) == False:
                            row['input_date'] = date_utils.get_date_to_string(data[2])
                            row['empresa_id'] = get_field(j, 'empresa')
                            row['rut_receptor'] = get_field(j, 'rut_receptor')
                            row['rut_emisor'] = get_field(j, 'rut_emisor')
                            row['tipo_envio'] = get_field(j, 'tipo_envio')
                            row['tipo_dte_id'] = get_field(j, 'tipo_dte')
                            row['numero_folio'] = get_field(j, 'numero_folio')
                            row['resolucion_receptor'] = get_field(j, 'resolucion_receptor')
                            row['resolucion_emisor'] = get_field(j, 'resolucion_emisor')
                            row['monto'] = get_field(j, 'monto')
                            row['fecha_emision'] = get_field(j, 'fecha_emision')
                            row['fecha_recepcion'] = get_field(j, 'fecha_recepcion')
                            row['estado_documento'] = get_field(j, 'estado_documento')
                            row['tipo_operacion'] = get_field(j, 'tipo_operacion')
                            row['tipo_receptor'] = get_field(j, 'tipo_receptor')
                            row['id_envio'] = get_field(j, 'id_envio')
                            row['nombre_cliente'] = get_field(j, 'nombre_cliente')
                            row['correo'] = get_row_field(data, 1)

                            row['smtp_id'] = get_row_field(data, 5)

                            evento = get_row_field(data, 0)
                            print "El evento es: " + evento

                            if evento == '"processed"':
                                row['processed_event'] = get_row_field(data, 0)
                                row['processed_date'] = get_row_field(data, 2)
                                row['processed_sg_event_id'] = get_row_field(data, 4)
                                row['processed_sg_message_id'] = get_row_field(data, 3)

                                # dejar campos en blanco
                                row['delivered_date'] = '""'
                                row['delivered_event'] = '""'
                                row['delivered_sg_event_id'] = '""'
                                row['delivered_sg_message_id'] = '""'
                                row['delivered_response'] = '""'

                                row['opened_first_date'] = '""'
                                row['opened_last_date'] = '""'
                                row['opened_event'] = '""'
                                row['opened_ip'] = '""'
                                row['opened_user_agent'] = '""'
                                row['opened_sg_event_id'] = '""'
                                row['opened_sg_message_id'] = '""'
                                row['opened_count'] = '""'

                                row['dropped_date'] = '""'
                                row['dropped_sg_event_id'] = '""'
                                row['dropped_sg_message_id'] = '""'
                                row['dropped_reason'] = '""'
                                row['dropped_event'] = '""'

                                row['bounce_date'] = '""'
                                row['bounce_event'] = '""'
                                row['bounce_sg_event_id'] = '""'
                                row['bounce_sg_message_id'] = '""'
                                row['bounce_reason'] = '""'
                                row['bounce_status'] = '""'
                                row['bounce_type'] = '""'

                                row['click_ip'] = '""'
                                row['click_purchase'] = '""'
                                row['click_useragent'] = '""'
                                row['click_event'] = '""'
                                row['click_email'] = '""'
                                row['click_date'] = '""'
                                row['click_url'] = '""'

                                csv_success.write(crear_linea_csv(CSV_HEADER_SUCCESS, row))

                            elif evento == '"delivered"':
                                row['delivered_date'] = get_row_field(data, 2)
                                row['delivered_event'] = get_row_field(data, 0)
                                row['delivered_sg_event_id'] = get_row_field(data, 4)
                                row['delivered_sg_message_id'] = get_row_field(data, 3)
                                row['delivered_response'] = get_row_field(data, 8)

                                row['processed_event'] = '""'
                                row['processed_date'] = '""'
                                row['processed_sg_event_id'] = '""'
                                row['processed_sg_message_id'] = '""'

                                row['opened_first_date'] = '""'
                                row['opened_last_date'] = '""'
                                row['opened_event'] = '""'
                                row['opened_ip'] = '""'
                                row['opened_user_agent'] = '""'
                                row['opened_sg_event_id'] = '""'
                                row['opened_sg_message_id'] = '""'
                                row['opened_count'] = '""'

                                row['dropped_date'] = '""'
                                row['dropped_sg_event_id'] = '""'
                                row['dropped_sg_message_id'] = '""'
                                row['dropped_reason'] = '""'
                                row['dropped_event'] = '""'

                                row['bounce_date'] = '""'
                                row['bounce_event'] = '""'
                                row['bounce_sg_event_id'] = '""'
                                row['bounce_sg_message_id'] = '""'
                                row['bounce_reason'] = '""'
                                row['bounce_status'] = '""'
                                row['bounce_type'] = '""'

                                row['click_ip'] = '""'
                                row['click_purchase'] = '""'
                                row['click_useragent'] = '""'
                                row['click_event'] = '""'
                                row['click_email'] = '""'
                                row['click_date'] = '""'
                                row['click_url'] = '""'

                                csv_success.write(crear_linea_csv(CSV_HEADER_SUCCESS, row))

                            elif evento == '"open"':
                                row['opened_first_date'] = get_row_field(data, 2)
                                row['opened_last_date'] = get_row_field(data, 2)
                                row['opened_event'] = get_row_field(data, 0)
                                row['opened_ip'] = get_row_field(data, 6)
                                row['opened_user_agent'] = get_row_field(data, 7)
                                row['opened_sg_event_id'] = get_row_field(data, 4)
                                row['opened_sg_message_id'] = get_row_field(data, 3)
                                row['opened_count'] = 1

                                row['processed_event'] = '""'
                                row['processed_date'] = '""'
                                row['processed_sg_event_id'] = '""'
                                row['processed_sg_message_id'] = '""'

                                row['delivered_date'] = '""'
                                row['delivered_event'] = '""'
                                row['delivered_sg_event_id'] = '""'
                                row['delivered_sg_message_id'] = '""'
                                row['delivered_response'] = '""'

                                row['dropped_date'] = '""'
                                row['dropped_sg_event_id'] = '""'
                                row['dropped_sg_message_id'] = '""'
                                row['dropped_reason'] = '""'
                                row['dropped_event'] = '""'

                                row['bounce_date'] = '""'
                                row['bounce_event'] = '""'
                                row['bounce_sg_event_id'] = '""'
                                row['bounce_sg_message_id'] = '""'
                                row['bounce_reason'] = '""'
                                row['bounce_status'] = '""'
                                row['bounce_type'] = '""'

                                row['click_ip'] = '""'
                                row['click_purchase'] = '""'
                                row['click_useragent'] = '""'
                                row['click_event'] = '""'
                                row['click_email'] = '""'
                                row['click_date'] = '""'
                                row['click_url'] = '""'

                                csv_success.write(crear_linea_csv(CSV_HEADER_SUCCESS, row))

                            elif evento == '"dropped"':
                                row['dropped_date'] = get_row_field(data, 2)
                                row['dropped_sg_event_id'] = get_row_field(data, 4)
                                row['dropped_sg_message_id'] = get_row_field(data, 3)
                                row['dropped_reason'] = get_row_field(data, 9)
                                row['dropped_event'] = get_row_field(data, 0)

                                row['processed_event'] = '""'
                                row['processed_date'] = '""'
                                row['processed_sg_event_id'] = '""'
                                row['processed_sg_message_id'] = '""'

                                row['delivered_date'] = '""'
                                row['delivered_event'] = '""'
                                row['delivered_sg_event_id'] = '""'
                                row['delivered_sg_message_id'] = '""'
                                row['delivered_response'] = '""'

                                row['opened_first_date'] = '""'
                                row['opened_last_date'] = '""'
                                row['opened_event'] = '""'
                                row['opened_ip'] = '""'
                                row['opened_user_agent'] = '""'
                                row['opened_sg_event_id'] = '""'
                                row['opened_sg_message_id'] = '""'
                                row['opened_count'] = '""'

                                row['bounce_date'] = '""'
                                row['bounce_event'] = '""'
                                row['bounce_sg_event_id'] = '""'
                                row['bounce_sg_message_id'] = '""'
                                row['bounce_reason'] = '""'
                                row['bounce_status'] = '""'
                                row['bounce_type'] = '""'

                                row['click_ip'] = '""'
                                row['click_purchase'] = '""'
                                row['click_useragent'] = '""'
                                row['click_event'] = '""'
                                row['click_email'] = '""'
                                row['click_date'] = '""'
                                row['click_url'] = '""'

                                csv_success.write(crear_linea_csv(CSV_HEADER_SUCCESS, row))

                            elif evento == '"bounce"':
                                row['bounce_date'] = get_row_field(data, 2)
                                row['bounce_event'] = get_row_field(data, 0)
                                row['bounce_sg_event_id'] = get_row_field(data, 4)
                                row['bounce_sg_message_id'] = get_row_field(data, 3)
                                row['bounce_reason'] = get_row_field(data, 9)
                                row['bounce_status'] = get_row_field(data, 10)
                                row['bounce_type'] = get_row_field(data, 11)

                                row['processed_event'] = '""'
                                row['processed_date'] = '""'
                                row['processed_sg_event_id'] = '""'
                                row['processed_sg_message_id'] = '""'

                                row['delivered_date'] = '""'
                                row['delivered_event'] = '""'
                                row['delivered_sg_event_id'] = '""'
                                row['delivered_sg_message_id'] = '""'
                                row['delivered_response'] = '""'

                                row['opened_first_date'] = '""'
                                row['opened_last_date'] = '""'
                                row['opened_event'] = '""'
                                row['opened_ip'] = '""'
                                row['opened_user_agent'] = '""'
                                row['opened_sg_event_id'] = '""'
                                row['opened_sg_message_id'] = '""'
                                row['opened_count'] = '""'

                                row['dropped_date'] = '""'
                                row['dropped_sg_event_id'] = '""'
                                row['dropped_sg_message_id'] = '""'
                                row['dropped_reason'] = '""'
                                row['dropped_event'] = '""'

                                row['click_ip'] = '""'
                                row['click_purchase'] = '""'
                                row['click_useragent'] = '""'
                                row['click_event'] = '""'
                                row['click_email'] = '""'
                                row['click_date'] = '""'
                                row['click_url'] = '""'

                                csv_success.write(crear_linea_csv(CSV_HEADER_SUCCESS, row))

                            elif evento == '"click"':
                                row['click_ip'] = get_row_field(data, 6)
                                row['click_purchase'] = '""'
                                row['click_useragent'] = '""'
                                row['click_event'] = get_row_field(data, 0)
                                row['click_email'] = '""'
                                row['click_date'] = get_row_field(data, 2)
                                row['click_url'] = get_row_field(data, 12)

                                row['processed_event'] = '""'
                                row['processed_date'] = '""'
                                row['processed_sg_event_id'] = '""'
                                row['processed_sg_message_id'] = '""'

                                row['delivered_date'] = '""'
                                row['delivered_event'] = '""'
                                row['delivered_sg_event_id'] = '""'
                                row['delivered_sg_message_id'] = '""'
                                row['delivered_response'] = '""'

                                row['opened_first_date'] = '""'
                                row['opened_last_date'] = '""'
                                row['opened_event'] = '""'
                                row['opened_ip'] = '""'
                                row['opened_user_agent'] = '""'
                                row['opened_sg_event_id'] = '""'
                                row['opened_sg_message_id'] = '""'
                                row['opened_count'] = '""'

                                row['dropped_date'] = '""'
                                row['dropped_sg_event_id'] = '""'
                                row['dropped_sg_message_id'] = '""'
                                row['dropped_reason'] = '""'
                                row['dropped_event'] = '""'

                                row['bounce_date'] = '""'
                                row['bounce_event'] = '""'
                                row['bounce_sg_event_id'] = '""'
                                row['bounce_sg_message_id'] = '""'
                                row['bounce_reason'] = '""'
                                row['bounce_status'] = '""'
                                row['bounce_type'] = '""'

                                row['click_ip'] = '""'
                                row['click_purchase'] = '""'
                                row['click_useragent'] = '""'
                                row['click_event'] = '""'
                                row['click_email'] = '""'
                                row['click_date'] = '""'
                                row['click_url'] = '""'

                                csv_success.write(crear_linea_csv(CSV_HEADER_SUCCESS, row))

                except Exception as e:
                    print e
                    raise e
        print "Proceso Finalizado"
    csv_errors.close()
    csv_success.close()
