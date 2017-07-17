# encoding: ISO-8859-1


import json
import date_utils


CSV_SUCCESS = "success.csv"


CSV_HEADER_SUCCESS = [
    'input_date', 'empresa_id', 'rut_receptor', 'rut_emisor', 'tipo_envio',
    'tipo_dte_id', 'numero_folio', 'resolucion_emisor',
    'monto', 'fecha_emision', 'estado_documento',
    'tipo_operacion', 'tipo_receptor', 'id_envio', 'nombre_cliente', 'correo',
    'smtp_id', 'processed_date', 'processed_event', 'processed_sg_event_id',
    'processed_sg_message_id', 'delivered_date', 'delivered_event',
    'delivered_sg_event_id', 'delivered_sg_message_id', 'delivered_response',
    'opened_first_date', 'opened_last_date', 'opened_event', 'opened_ip',
    'opened_user_agent', 'opened_sg_event_id', 'opened_sg_message_id',
    'opened_count', 'dropped_date', 'dropped_sg_event_id',
    'dropped_sg_message_id', 'dropped_reason', 'dropped_event', 'bounce_date',
    'bounce_event', 'bounce_sg_event_id', 'bounce_sg_message_id',
    'bounce_reason', 'bounce_status', 'bounce_type'
]


def exist_empresa(row):
    print "Validando existencia de Empresa en JSON"
    try:
        val = row['empresa']
        if val:
            return True
        else:
            return False
    except Exception as e:
        print e
        return False


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
            return 'NULL'


def get_field(obj, field):
    print "Convirtiendo " + field
    if obj is not None:
        try:
            return '"' + str(obj[field]) + '"'
        except Exception as e:
            print e
            return 'NULL'
    else:
        return 'NULL'


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
            linea += str('NULL') + ','
    linea = linea[:-1]
    print "IMPRIMIENDO LINEA : " + str(linea) + "\n"
    return linea + "\n"


def generar_csv(reader):
    primer_row = ['processed', 'delivered', 'open', 'bounce', 'dropped']
    cantidad_documentos = 0
    csv_success = open(CSV_SUCCESS, "w")
    csv_success.write(get_header(CSV_HEADER_SUCCESS))

    print "Cabeceras creadas"

    if reader is not None:
        for data in reader:
            e = data[0]
            e = str(e).replace('"', '')
            if e in primer_row:
                print data

                if data[18]:
                    j = json.loads(data[18])

                    if exist_empresa(j):
                        row = dict()
                        row['input_date'] = date_utils.get_date_to_string(data[2])
                        row['empresa_id'] = get_field(j, 'empresa')
                        row['rut_receptor'] = get_field(j, 'rut_receptor')
                        row['rut_emisor'] = get_field(j, 'rut_emisor')
                        row['tipo_envio'] = get_field(j, 'tipo_envio')
                        row['tipo_dte_id'] = get_field(j, 'tipo_dte')
                        row['numero_folio'] = get_field(j, 'numero_folio')
                        row['resolucion_emisor'] = get_field(j, 'resolucion_emisor')
                        row['monto'] = get_field(j, 'monto')
                        row['fecha_emision'] = get_field(j, 'fecha_emision')
                        row['estado_documento'] = get_field(j, 'estado_documento')
                        row['tipo_operacion'] = get_field(j, 'tipo_operacion')
                        row['tipo_receptor'] = get_field(j, 'tipo_receptor')
                        row['id_envio'] = get_field(j, 'id_envio')
                        correo = get_row_field(data, 1)
                        row['correo'] = correo
                        nombre_cliente = get_field(j, 'nombre_cliente')
                        if nombre_cliente is not 'NULL':
                            row['nombre_cliente'] = nombre_cliente
                        else:
                            row['nombre_cliente'] = correo

                        row['smtp_id'] = get_row_field(data, 7)

                        evento = get_row_field(data, 0)
                        evento = evento.replace('"', '')
                        print "El evento es: " + evento

                        if evento == 'processed':
                            row['processed_event'] = get_row_field(data, 0)
                            row['processed_date'] = get_row_field(data, 2)
                            row['processed_sg_event_id'] = get_row_field(data, 6)
                            row['processed_sg_message_id'] = get_row_field(data, 4)

                            # dejar campos en blanco
                            row['delivered_date'] = 'NULL'
                            row['delivered_event'] = 'NULL'
                            row['delivered_sg_event_id'] = 'NULL'
                            row['delivered_sg_message_id'] = 'NULL'
                            row['delivered_response'] = 'NULL'

                            row['opened_first_date'] = 'NULL'
                            row['opened_last_date'] = 'NULL'
                            row['opened_event'] = 'NULL'
                            row['opened_ip'] = 'NULL'
                            row['opened_user_agent'] = 'NULL'
                            row['opened_sg_event_id'] = 'NULL'
                            row['opened_sg_message_id'] = 'NULL'
                            row['opened_count'] = '"0"'

                            row['dropped_date'] = 'NULL'
                            row['dropped_sg_event_id'] = 'NULL'
                            row['dropped_sg_message_id'] = 'NULL'
                            row['dropped_reason'] = 'NULL'
                            row['dropped_event'] = 'NULL'

                            row['bounce_date'] = 'NULL'
                            row['bounce_event'] = 'NULL'
                            row['bounce_sg_event_id'] = 'NULL'
                            row['bounce_sg_message_id'] = 'NULL'
                            row['bounce_reason'] = 'NULL'
                            row['bounce_status'] = 'NULL'
                            row['bounce_type'] = 'NULL'

                            cantidad_documentos += 1
                            csv_success.write(crear_linea_csv(CSV_HEADER_SUCCESS, row))

                        elif evento == 'delivered':
                            row['delivered_date'] = get_row_field(data, 2)
                            row['delivered_event'] = get_row_field(data, 0)
                            row['delivered_sg_event_id'] = get_row_field(data, 6)
                            row['delivered_sg_message_id'] = get_row_field(data, 4)
                            row['delivered_response'] = get_row_field(data, 10)

                            row['processed_event'] = 'NULL'
                            row['processed_date'] = 'NULL'
                            row['processed_sg_event_id'] = 'NULL'
                            row['processed_sg_message_id'] = 'NULL'

                            row['opened_first_date'] = 'NULL'
                            row['opened_last_date'] = 'NULL'
                            row['opened_event'] = 'NULL'
                            row['opened_ip'] = 'NULL'
                            row['opened_user_agent'] = 'NULL'
                            row['opened_sg_event_id'] = 'NULL'
                            row['opened_sg_message_id'] = 'NULL'
                            row['opened_count'] = '"0"'

                            row['dropped_date'] = 'NULL'
                            row['dropped_sg_event_id'] = 'NULL'
                            row['dropped_sg_message_id'] = 'NULL'
                            row['dropped_reason'] = 'NULL'
                            row['dropped_event'] = 'NULL'

                            row['bounce_date'] = 'NULL'
                            row['bounce_event'] = 'NULL'
                            row['bounce_sg_event_id'] = 'NULL'
                            row['bounce_sg_message_id'] = 'NULL'
                            row['bounce_reason'] = 'NULL'
                            row['bounce_status'] = 'NULL'
                            row['bounce_type'] = 'NULL'

                            cantidad_documentos += 1
                            csv_success.write(crear_linea_csv(CSV_HEADER_SUCCESS, row))

                        elif evento == 'open':
                            row['opened_first_date'] = get_row_field(data, 2)
                            row['opened_last_date'] = get_row_field(data, 2)
                            row['opened_event'] = get_row_field(data, 0)
                            row['opened_ip'] = get_row_field(data, 8)
                            row['opened_user_agent'] = get_row_field(data, 9)
                            row['opened_sg_event_id'] = get_row_field(data, 6)
                            row['opened_sg_message_id'] = get_row_field(data, 4)
                            row['opened_count'] = '"1"'

                            row['processed_event'] = 'NULL'
                            row['processed_date'] = 'NULL'
                            row['processed_sg_event_id'] = 'NULL'
                            row['processed_sg_message_id'] = 'NULL'

                            row['delivered_date'] = 'NULL'
                            row['delivered_event'] = 'NULL'
                            row['delivered_sg_event_id'] = 'NULL'
                            row['delivered_sg_message_id'] = 'NULL'
                            row['delivered_response'] = 'NULL'

                            row['dropped_date'] = 'NULL'
                            row['dropped_sg_event_id'] = 'NULL'
                            row['dropped_sg_message_id'] = 'NULL'
                            row['dropped_reason'] = 'NULL'
                            row['dropped_event'] = 'NULL'

                            row['bounce_date'] = 'NULL'
                            row['bounce_event'] = 'NULL'
                            row['bounce_sg_event_id'] = 'NULL'
                            row['bounce_sg_message_id'] = 'NULL'
                            row['bounce_reason'] = 'NULL'
                            row['bounce_status'] = 'NULL'
                            row['bounce_type'] = 'NULL'

                            cantidad_documentos += 1
                            csv_success.write(crear_linea_csv(CSV_HEADER_SUCCESS, row))

                        elif evento == 'dropped':
                            row['dropped_date'] = get_row_field(data, 2)
                            row['dropped_sg_event_id'] = get_row_field(data, 6)
                            row['dropped_sg_message_id'] = get_row_field(data, 4)
                            row['dropped_reason'] = get_row_field(data, 11)
                            row['dropped_event'] = get_row_field(data, 0)

                            row['processed_event'] = 'NULL'
                            row['processed_date'] = 'NULL'
                            row['processed_sg_event_id'] = 'NULL'
                            row['processed_sg_message_id'] = 'NULL'

                            row['delivered_date'] = 'NULL'
                            row['delivered_event'] = 'NULL'
                            row['delivered_sg_event_id'] = 'NULL'
                            row['delivered_sg_message_id'] = 'NULL'
                            row['delivered_response'] = 'NULL'

                            row['opened_first_date'] = 'NULL'
                            row['opened_last_date'] = 'NULL'
                            row['opened_event'] = 'NULL'
                            row['opened_ip'] = 'NULL'
                            row['opened_user_agent'] = 'NULL'
                            row['opened_sg_event_id'] = 'NULL'
                            row['opened_sg_message_id'] = 'NULL'
                            row['opened_count'] = 'NULL'

                            row['bounce_date'] = 'NULL'
                            row['bounce_event'] = 'NULL'
                            row['bounce_sg_event_id'] = 'NULL'
                            row['bounce_sg_message_id'] = 'NULL'
                            row['bounce_reason'] = 'NULL'
                            row['bounce_status'] = 'NULL'
                            row['bounce_type'] = 'NULL'

                            cantidad_documentos += 1
                            csv_success.write(crear_linea_csv(CSV_HEADER_SUCCESS, row))

                        elif evento == 'bounce':
                            row['bounce_date'] = get_row_field(data, 2)
                            row['bounce_event'] = get_row_field(data, 0)
                            row['bounce_sg_event_id'] = get_row_field(data, 6)
                            row['bounce_sg_message_id'] = get_row_field(data, 4)
                            row['bounce_reason'] = get_row_field(data, 11)
                            row['bounce_status'] = get_row_field(data, 13)
                            row['bounce_type'] = get_row_field(data, 14)

                            row['processed_event'] = 'NULL'
                            row['processed_date'] = 'NULL'
                            row['processed_sg_event_id'] = 'NULL'
                            row['processed_sg_message_id'] = 'NULL'

                            row['delivered_date'] = 'NULL'
                            row['delivered_event'] = 'NULL'
                            row['delivered_sg_event_id'] = 'NULL'
                            row['delivered_sg_message_id'] = 'NULL'
                            row['delivered_response'] = 'NULL'

                            row['opened_first_date'] = 'NULL'
                            row['opened_last_date'] = 'NULL'
                            row['opened_event'] = 'NULL'
                            row['opened_ip'] = 'NULL'
                            row['opened_user_agent'] = 'NULL'
                            row['opened_sg_event_id'] = 'NULL'
                            row['opened_sg_message_id'] = 'NULL'
                            row['opened_count'] = '"0"'

                            row['dropped_date'] = 'NULL'
                            row['dropped_sg_event_id'] = 'NULL'
                            row['dropped_sg_message_id'] = 'NULL'
                            row['dropped_reason'] = 'NULL'
                            row['dropped_event'] = 'NULL'

                            cantidad_documentos += 1
                            csv_success.write(crear_linea_csv(CSV_HEADER_SUCCESS, row))

        print "Proceso Finalizado con : " + str(cantidad_documentos) + " registros."
    csv_success.close()
