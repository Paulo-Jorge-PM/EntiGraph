#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from argparse import ArgumentParser
from gooey import Gooey, GooeyParser#GUI

#To ignore the GUI and run in CLI run with --ignore-gooey e.g.:
#pythonw --ignore-gooey run.py --fileName xxx etc.

import iterate

@Gooey(
    program_name="EntiGraph",
    program_description="Identify entities and generate RDF graphs",
    default_size=(600, 720),
    #fullscreen=True,

    #progress_regex=r"^progress: (?P<current>\d+)/(?P<total>\d+)$",
    #progress_expr="current / total * 100"
    #, hide_progress_msg=True
    #navigation="TABBED",
)

def cli():
        parser = GooeyParser(description="EntiGraph Configurations")
        mandatory = parser.add_argument_group('Mandatory parameters')
        optional = parser.add_argument_group('Optional parameters')

        mandatory.add_argument(
            "-i",
            "--fileName",
            required=True,
            metavar="Input",
            help="Input file.",

            #Gooey extra arguments:
            widget="FileChooser",
            gooey_options=dict(wildcard="JSON (*.json)|*.json")
        )
        mandatory.add_argument(
            "-w",
            "--workFolder",
            required=True,
            metavar="Output",
            help="Output file.",

            #Gooey extra arguments:
            widget="FileSaver",
            gooey_options=dict(wildcard="Turtle (.ttl)|*.ttl")
        )

        optional.add_argument(
            "-c",
            "--mainClass",
            required=False,
            metavar="Class Name",
            default="Article",
            help="Default graph class name.",

            #Gooey extra arguments:
            action="store"
        )
        optional.add_argument(
            "-a",
            "--allFolder",
            required=False,
            metavar="Iterate all folder?",
            help="Include all sibling files in folder?" ,

            #Gooey extra arguments:
            action="store_true"
        )
        optional.add_argument(
            "-s",
            "--skeleton",
            required=False,
            metavar="RDF Skeleton",
            help="Default ontology skeleton.",
            default=os.path.join(os.getcwd(), "ontology_skeleton.ttl"),

            #Gooey extra arguments:
            widget="FileChooser",
            gooey_options=dict(wildcard="Turtle (.ttl)|*.ttl")
        )
        optional.add_argument(
            "-sa",
            "--sentiment",
            required=False,
            metavar="Sentiment Analysis?",
            help="Include Sentiment Analysis?",

            #Gooey extra arguments:
            action="store_true"
        )
        optional.add_argument(
            "-u",
            "--uri",
            required=False,
            metavar="RDF URI",
            default="http://sparql.entigraph.di.pt/corpus",
            help="Default URI.",

            #Gooey extra arguments:
            action="store"
        )
        optional.add_argument(
            "-l",
            "--sourceLang",
            required=False,
            metavar="Source Language",
            default="pt",
            help="Text language (for Sentiment Analysis).",

            #Gooey extra arguments:
            action="store"
        )


        args = parser.parse_args()

        print(args.fileName)
        print(args.allFolder)
        print(args.workFolder)
        print(args.mainClass)
        print(args.skeleton)
        print(args.sentiment)

        """
        iterate.Iterate(fileName=args.fileName, 
        allFolder=args.allFolder, 
        workFolder=args.workFolder, 
        mainClass=args.mainClass, 
        skeleton=args.skeleton, 
        sentiment=args.sentiment)
        """
if __name__ == "__main__":
    cli()
