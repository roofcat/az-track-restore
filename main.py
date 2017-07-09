# encoding:utf-8
#!/usr/bin/env python


import csv
import json
import os
from optparse import OptionParser


from csv_loads import generar_csv


def main():
    usage = """python main.py --file=SENDGRID_CSV_FILE"""
    parser = OptionParser(usage=usage)
    parser.add_option('-f', '--file', default=None, metavar='FILE',
                      dest='file', help='Archivo CSV SendGrid')
    options, args = parser.parse_args()

    if args:
        parser.print_help()
        parser.exit(msg='\nArgumentos no esperados: %s ' % ' '.join(args))

    csv_file = options.file

    if csv_file:
        try:
            print csv_file
            archivo = open(csv_file, 'rbU')
            reader = csv.reader(archivo, delimiter=';')

            generar_csv(reader)

        except IOError as ioe:
            parser.error('Error al abrir archivo csv.')
        except Exception as ex:
            print ex
            parser.error('Ha ocurrido un error ' + ex.message)
    else:
        print 'Debes ingresar nombre de archivo CSV.'

if __name__ == '__main__':
    main()
